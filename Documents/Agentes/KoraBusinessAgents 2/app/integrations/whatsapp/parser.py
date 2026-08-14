from dataclasses import dataclass
from typing import Any
from typing import Any, Optional


@dataclass
class ParsedWhatsAppMessage:
    message_id: str
    phone: str
    text: str


def parse_incoming_text_message(payload: dict[str, Any]) -> Optional[ParsedWhatsAppMessage]:
    try:
        entries = payload.get("entry", [])
        for entry in entries:
            for change in entry.get("changes", []):
                value = change.get("value", {})
                messages = value.get("messages", [])

                if not messages:
                    return None

                message = messages[0]
                if message.get("type") != "text":
                    return None

                return ParsedWhatsAppMessage(
                    message_id=message["id"],
                    phone=message["from"],
                    text=message.get("text", {}).get("body", ""),
                )

        return None

    except (KeyError, TypeError, IndexError):
        return None
