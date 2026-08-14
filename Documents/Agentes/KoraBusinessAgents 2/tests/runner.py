"""
tests/runner.py

Motor de ejecución. No tocar al añadir nuevos test cases.

Uso:
    python tests/runner.py                 # todos los casos
    python tests/runner.py --id PRM-001   # un caso concreto
    python tests/runner.py --tag reserva  # por tag
    python tests/runner.py --no-excel     # sin Excel
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sqlite3
import sys
import time
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from tests.assertions import check_turn
from tests.report import CaseReport, TurnReport, print_results, update_inventory

# ------------------------------------------------------------------ #
#  Config                                                              #
# ------------------------------------------------------------------ #

WEBHOOK_URL   = os.getenv("WEBHOOK_URL",   "http://localhost:8000/webhook/whatsapp")
DB_PATH       = os.getenv("DB_PATH",       "mvp.db")
CASES_DIR     = os.getenv("CASES_DIR",     "tests/cases")
POLL_TIMEOUT  = float(os.getenv("POLL_TIMEOUT",  "8"))
POLL_INTERVAL = float(os.getenv("POLL_INTERVAL", "0.3"))

_phone_counter = 34_699_000_000


def _next_phone() -> str:
    global _phone_counter
    _phone_counter += 1
    return str(_phone_counter)


# ------------------------------------------------------------------ #
#  Base de datos                                                       #
# ------------------------------------------------------------------ #

def _db() -> sqlite3.Connection:
    candidates = [
        DB_PATH,
        "app.db",
        "data/mvp.db",
        os.path.join(os.path.dirname(__file__), "..", "mvp.db"),
        os.path.join(os.path.dirname(__file__), "..", "app.db"),
    ]
    path = next((p for p in candidates if os.path.exists(p)), None)
    if not path:
        raise FileNotFoundError(
            "No se encontró la BD. Define DB_PATH=<ruta> como variable de entorno."
        )
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def _last_outbound_rowid(phone: str) -> int:
    """Rowid del último outbound existente para este teléfono (0 si ninguno)."""
    conn = _db()
    row  = conn.execute(
        "SELECT id FROM messages WHERE phone=? AND direction='outbound' ORDER BY id DESC LIMIT 1",
        (phone,),
    ).fetchone()
    conn.close()
    return row["id"] if row else 0


def _poll_outbound(phone: str, after_rowid: int) -> str | None:
    """
    Espera hasta POLL_TIMEOUT segundos a que aparezca un nuevo outbound
    para este teléfono con id > after_rowid. Devuelve body o None si timeout.

    Estrategia: polling cada POLL_INTERVAL segundos.
    Funciona porque MessageProcessor hace save_state ANTES de insert_outbound,
    por lo que cuando el outbound aparece, el estado ya está persistido.
    """
    deadline = time.time() + POLL_TIMEOUT
    while time.time() < deadline:
        conn = _db()
        row  = conn.execute(
            """
            SELECT id, body FROM messages
            WHERE phone=? AND direction='outbound' AND id > ?
            ORDER BY id ASC LIMIT 1
            """,
            (phone, after_rowid),
        ).fetchone()
        conn.close()
        if row:
            return row["body"]
        time.sleep(POLL_INTERVAL)
    return None


def _get_stage(phone: str) -> str:
    """Lee el stage del estado de conversación en BD."""
    conn = _db()
    row  = conn.execute(
        "SELECT state_json FROM conversations WHERE phone=?",
        (phone,),
    ).fetchone()
    conn.close()
    if not row:
        return "UNKNOWN"
    return json.loads(row["state_json"]).get("stage", "UNKNOWN")


# ------------------------------------------------------------------ #
#  Envío                                                               #
# ------------------------------------------------------------------ #

def _send(phone: str, body: str, msg_id: str) -> None:
    import urllib.request
    payload = json.dumps({"entry": [{"changes": [{"value": {"messages": [{
        "id":        msg_id,
        "from":      phone,
        "timestamp": str(int(time.time())),
        "type":      "text",
        "text":      {"body": body},
    }]}}]}]}).encode()

    req = urllib.request.Request(
        WEBHOOK_URL, data=payload,
        headers={"Content-Type": "application/json"}, method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        if resp.status not in (200, 201, 202):
            raise RuntimeError(f"Webhook devolvió HTTP {resp.status}")


# ------------------------------------------------------------------ #
#  Ejecución de un caso                                                #
# ------------------------------------------------------------------ #

def run_case(case_data: dict, file_path: str) -> CaseReport:
    phone  = _next_phone()
    t0     = time.time()

    report = CaseReport(
        case_id     = case_data["id"],
        case_type   = case_data.get("type", "VALID"),
        description = case_data.get("description", ""),
        file_path   = file_path,
        passed      = True,
    )

    try:
        for i, turn_cfg in enumerate(case_data.get("turns", [])):
            user_msg   = turn_cfg["user"]
            assert_cfg = turn_cfg.get("assert", {})
            msg_id     = f"wamid.{case_data['id']}_{phone}_{i:03d}"

            last_rowid = _last_outbound_rowid(phone)
            _send(phone, user_msg, msg_id)

            reply = _poll_outbound(phone, after_rowid=last_rowid)

            if reply is None:
                report.turns.append(TurnReport(
                    turn_number=i + 1, user_message=user_msg,
                    reply="", stage="TIMEOUT", passed=False,
                    failures=[f"Sin respuesta outbound tras {POLL_TIMEOUT}s"],
                ))
                report.passed = False
                break

            stage  = _get_stage(phone)
            result = check_turn(reply=reply, stage=stage, assert_config=assert_cfg)

            report.turns.append(TurnReport(
                turn_number=i + 1, user_message=user_msg,
                reply=reply, stage=stage,
                passed=result.passed, failures=result.failures,
            ))

            if not result.passed:
                report.passed = False
                break

    except Exception as exc:
        report.passed = False
        report.error  = str(exc)

    report.duration_ms = int((time.time() - t0) * 1000)
    return report


# ------------------------------------------------------------------ #
#  Carga de casos                                                      #
# ------------------------------------------------------------------ #

def load_cases(filter_id: str | None, filter_tag: str | None) -> list[tuple[dict, str]]:
    files = sorted(glob.glob(os.path.join(CASES_DIR, "*.json")))
    if not files:
        print(f"\n  ⚠  No se encontraron JSONs en '{CASES_DIR}'\n")
        sys.exit(1)

    cases = []
    for path in files:
        with open(path) as f:
            data = json.load(f)
        if filter_id  and data.get("id")       != filter_id:
            continue
        if filter_tag and filter_tag not in data.get("tags", []):
            continue
        cases.append((data, path))

    return cases


# ------------------------------------------------------------------ #
#  Entry point                                                         #
# ------------------------------------------------------------------ #

def main() -> None:
    parser = argparse.ArgumentParser(description="Dental Agent — Test Runner")
    parser.add_argument("--id",       help="Ejecutar solo el caso con este ID")
    parser.add_argument("--tag",      help="Ejecutar solo los casos con este tag")
    parser.add_argument("--no-excel", action="store_true", help="No generar inventario Excel")
    args = parser.parse_args()

    cases = load_cases(filter_id=args.id, filter_tag=args.tag)
    print(f"\n  Cargados {len(cases)} caso(s).\n")

    reports = []
    for case_data, file_path in cases:
        label = f"{case_data['id']} — {case_data['description'][:40]}"
        sys.stdout.write(f"  ⏳  {label}\r")
        sys.stdout.flush()
        reports.append(run_case(case_data, file_path))

    print_results(reports)

    if not args.no_excel:
        update_inventory(reports)

    sys.exit(0 if all(r.passed for r in reports) else 1)


if __name__ == "__main__":
    main()