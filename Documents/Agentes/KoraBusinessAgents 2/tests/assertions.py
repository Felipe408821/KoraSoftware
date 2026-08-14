"""
tests/assertions.py

Lógica de verificación para cada turno.
No tocar al añadir nuevos test cases salvo que se incorporen nuevas dimensiones de validación.

Soporta:
  stage              — stage exacto esperado tras el turno
  mode               — mode exacto esperado en conversations
  status             — status exacto esperado en conversations
  reply_contains_any — al menos uno de los fragmentos aparece en reply
  reply_contains_all — todos los fragmentos aparecen en reply
  reply_excludes     — ninguno de los fragmentos aparece en reply
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class AssertionResult:
    passed: bool
    failures: list[str] = field(default_factory=list)


def check_turn(
    *,
    reply: str,
    stage: str,
    assert_config: dict,
    mode: str | None = None,
    status: str | None = None,
) -> AssertionResult:
    """
    Verifica las assertions de un turno.

    Compatible hacia atrás:
    - Los test cases antiguos que solo validan stage/reply siguen funcionando.
    - Los nuevos test cases pueden añadir mode/status.
    """

    failures: list[str] = []
    reply_low = (reply or "").lower()

    # stage
    expected_stage = assert_config.get("stage")
    if expected_stage and stage != expected_stage:
        failures.append(
            f"stage → esperado: '{expected_stage}' | obtenido: '{stage}'"
        )

    # mode
    expected_mode = assert_config.get("mode")
    if expected_mode and mode != expected_mode:
        failures.append(
            f"mode → esperado: '{expected_mode}' | obtenido: '{mode}'"
        )

    # status
    expected_status = assert_config.get("status")
    if expected_status and status != expected_status:
        failures.append(
            f"status → esperado: '{expected_status}' | obtenido: '{status}'"
        )

    # reply_contains_any
    contains_any = assert_config.get("reply_contains_any", [])
    if contains_any and not any(fragment.lower() in reply_low for fragment in contains_any):
        failures.append(
            f"reply_contains_any → ninguno encontrado en reply: {contains_any}"
        )

    # reply_contains_all
    for fragment in assert_config.get("reply_contains_all", []):
        if fragment.lower() not in reply_low:
            failures.append(f"reply_contains_all → falta: '{fragment}'")

    # reply_excludes
    for fragment in assert_config.get("reply_excludes", []):
        if fragment.lower() in reply_low:
            failures.append(f"reply_excludes → no debería contener: '{fragment}'")

    return AssertionResult(
        passed=len(failures) == 0,
        failures=failures,
    )