import json
from datetime import datetime, timezone
from typing import Any

from app.storage.sqlite import get_connection
from app.agent.state_factory import initial_state


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class ConversationRepository:
    def get_or_create_state(
        self,
        *,
        phone: str,
        clinic_id: str = "clinic_demo",
    ) -> dict[str, Any]:
        with get_connection() as conn:
            row = conn.execute(
                "SELECT state_json FROM conversations WHERE phone = ?",
                (phone,),
            ).fetchone()

            if row:
                return json.loads(row["state_json"])

            state = initial_state(phone=phone, clinic_id=clinic_id)

            now = utc_now()
            conn.execute(
                """
                INSERT INTO conversations (
                    phone,
                    clinic_id,
                    state_json,
                    mode,
                    status,
                    paused_until,
                    assigned_to,
                    handoff_reason,
                    last_message_at,
                    last_message_preview,
                    created_at,
                    updated_at
                )
                VALUES (?, ?, ?, 'AUTO', 'OPEN', NULL, NULL, NULL, NULL, NULL, ?, ?)
                """,
                (
                    phone,
                    clinic_id,
                    json.dumps(state, ensure_ascii=False),
                    now,
                    now,
                ),
            )
            conn.commit()

            return state

    def save_state(
        self,
        *,
        phone: str,
        state: dict[str, Any],
        clinic_id: str = "clinic_demo",
    ) -> None:
        now = utc_now()

        with get_connection() as conn:
            conn.execute(
                """
                INSERT INTO conversations (
                    phone,
                    clinic_id,
                    state_json,
                    mode,
                    status,
                    paused_until,
                    assigned_to,
                    handoff_reason,
                    last_message_at,
                    last_message_preview,
                    created_at,
                    updated_at
                )
                VALUES (?, ?, ?, 'AUTO', 'OPEN', NULL, NULL, NULL, NULL, NULL, ?, ?)
                ON CONFLICT(phone) DO UPDATE SET
                    clinic_id = excluded.clinic_id,
                    state_json = excluded.state_json,
                    updated_at = excluded.updated_at
                """,
                (
                    phone,
                    clinic_id,
                    json.dumps(state, ensure_ascii=False),
                    now,
                    now,
                ),
            )
            conn.commit()

    def get_conversation_by_phone(self, *, phone: str) -> dict[str, Any] | None:
        with get_connection() as conn:
            row = conn.execute(
                """
                SELECT
                    id,
                    phone,
                    clinic_id,
                    state_json,
                    mode,
                    status,
                    paused_until,
                    assigned_to,
                    handoff_reason,
                    last_message_at,
                    last_message_preview,
                    created_at,
                    updated_at
                FROM conversations
                WHERE phone = ?
                """,
                (phone,),
            ).fetchone()

        if row is None:
            return None

        return {
            "id": row["id"],
            "phone": row["phone"],
            "clinic_id": row["clinic_id"],
            "state_json": row["state_json"],
            "state": json.loads(row["state_json"]),
            "mode": row["mode"],
            "status": row["status"],
            "paused_until": row["paused_until"],
            "assigned_to": row["assigned_to"],
            "handoff_reason": row["handoff_reason"],
            "last_message_at": row["last_message_at"],
            "last_message_preview": row["last_message_preview"],
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
        }

    def mark_pending_human(
        self,
        *,
        phone: str,
        reason: str,
        assigned_to: str | None = None,
    ) -> None:
        now = utc_now()

        with get_connection() as conn:
            conn.execute(
                """
                UPDATE conversations
                SET
                    mode = 'HUMAN',
                    status = 'PENDING_HUMAN',
                    paused_until = NULL,
                    assigned_to = ?,
                    handoff_reason = ?,
                    updated_at = ?
                WHERE phone = ?
                """,
                (
                    assigned_to,
                    reason,
                    now,
                    phone,
                ),
            )
            conn.commit()

    def release_to_bot(self, *, phone: str) -> None:
        now = utc_now()

        with get_connection() as conn:
            conn.execute(
                """
                UPDATE conversations
                SET
                    mode = 'AUTO',
                    status = 'OPEN',
                    paused_until = NULL,
                    assigned_to = NULL,
                    handoff_reason = 'released_to_bot',
                    updated_at = ?
                WHERE phone = ?
                """,
                (
                    now,
                    phone,
                ),
            )
            conn.commit()

    def pause_conversation(
        self,
        *,
        phone: str,
        paused_until: str | None,
        reason: str = "manual_pause",
    ) -> None:
        now = utc_now()

        with get_connection() as conn:
            conn.execute(
                """
                UPDATE conversations
                SET
                    mode = 'PAUSED',
                    status = 'OPEN',
                    paused_until = ?,
                    assigned_to = NULL,
                    handoff_reason = ?,
                    updated_at = ?
                WHERE phone = ?
                """,
                (
                    paused_until,
                    reason,
                    now,
                    phone,
                ),
            )
            conn.commit()

    def close_conversation(
        self,
        *,
        phone: str,
        reason: str = "conversation_closed",
    ) -> None:
        now = utc_now()

        with get_connection() as conn:
            conn.execute(
                """
                UPDATE conversations
                SET
                    mode = 'AUTO',
                    status = 'CLOSED',
                    paused_until = NULL,
                    assigned_to = NULL,
                    handoff_reason = ?,
                    updated_at = ?
                WHERE phone = ?
                """,
                (
                    reason,
                    now,
                    phone,
                ),
            )
            conn.commit()

    def touch_last_message(
        self,
        *,
        phone: str,
        preview: str,
    ) -> None:
        now = utc_now()

        with get_connection() as conn:
            conn.execute(
                """
                UPDATE conversations
                SET
                    last_message_at = ?,
                    last_message_preview = ?,
                    updated_at = ?
                WHERE phone = ?
                """,
                (
                    now,
                    preview[:300],
                    now,
                    phone,
                ),
            )
            conn.commit()