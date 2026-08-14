from datetime import datetime, timezone

from app.storage.sqlite import get_connection


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class MessageRepository:
    def insert_inbound_if_new(
        self,
        *,
        whatsapp_message_id: str,
        phone: str,
        body: str,
    ) -> bool:
        now = utc_now()

        with get_connection() as conn:
            cursor = conn.execute(
                """
                INSERT OR IGNORE INTO messages (
                    whatsapp_message_id,
                    phone,
                    direction,
                    body,
                    status,
                    created_at,
                    updated_at
                )
                VALUES (?, ?, 'inbound', ?, 'received', ?, ?)
                """,
                (whatsapp_message_id, phone, body, now, now),
            )

            conn.commit()
            return cursor.rowcount == 1

    def mark_processing(self, whatsapp_message_id: str) -> None:
        self._update_status(whatsapp_message_id, "processing")

    def mark_processed(self, whatsapp_message_id: str) -> None:
        self._update_status(whatsapp_message_id, "processed")

    def mark_failed(self, whatsapp_message_id: str) -> None:
        self._update_status(whatsapp_message_id, "failed")

    def _update_status(self, whatsapp_message_id: str, status: str) -> None:
        now = utc_now()

        with get_connection() as conn:
            conn.execute(
                """
                UPDATE messages
                SET status = ?, updated_at = ?
                WHERE whatsapp_message_id = ?
                """,
                (status, now, whatsapp_message_id),
            )
            conn.commit()

    def insert_outbound(
        self,
        *,
        phone: str,
        body: str,
        status: str = "sent",
    ) -> int:
        now = utc_now()

        with get_connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO messages (
                    whatsapp_message_id,
                    phone,
                    direction,
                    body,
                    status,
                    created_at,
                    updated_at
                )
                VALUES (?, ?, 'outbound', ?, ?, ?, ?)
                """,
                (None, phone, body, status, now, now),
            )

            conn.commit()
            return int(cursor.lastrowid)

    def get_recent_messages(self, phone: str, limit: int = 10) -> list[dict]:
        with get_connection() as conn:
            rows = conn.execute(
                """
                SELECT id, direction, body, status, created_at
                FROM messages
                WHERE phone = ?
                ORDER BY id DESC
                LIMIT ?
                """,
                (phone, limit),
            ).fetchall()

        return [dict(row) for row in reversed(rows)]