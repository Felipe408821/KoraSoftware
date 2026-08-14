from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.storage.sqlite import get_connection


def main() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                whatsapp_message_id TEXT UNIQUE,
                phone TEXT NOT NULL,
                direction TEXT NOT NULL,
                body TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone TEXT NOT NULL UNIQUE,
                clinic_id TEXT NOT NULL,
                state_json TEXT NOT NULL,

                mode TEXT NOT NULL DEFAULT 'AUTO',
                status TEXT NOT NULL DEFAULT 'OPEN',
                paused_until TEXT,
                assigned_to TEXT,
                handoff_reason TEXT,

                last_message_at TEXT,
                last_message_preview TEXT,

                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                clinic_id TEXT NOT NULL,
                patient_name TEXT NOT NULL,
                patient_phone TEXT NOT NULL,
                treatment_id TEXT NOT NULL,
                professional_id TEXT NOT NULL,
                resource_id TEXT NOT NULL,
                start_datetime TEXT NOT NULL,
                end_datetime TEXT NOT NULL,
                google_event_id TEXT,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tool_calls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                clinic_id TEXT NOT NULL,
                phone TEXT,
                tool_name TEXT NOT NULL,
                input_json TEXT,
                output_json TEXT,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL
            );
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS audit_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                clinic_id TEXT NOT NULL,
                entity_type TEXT NOT NULL,
                entity_id TEXT,
                action TEXT NOT NULL,
                metadata_json TEXT,
                created_at TEXT NOT NULL
            );
            """
        )

        conn.commit()

    print("SQLite inicializado correctamente.")


if __name__ == "__main__":
    main()