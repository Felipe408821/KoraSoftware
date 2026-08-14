from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class AgentResult:
    reply: str
    new_state: dict[str, Any]
