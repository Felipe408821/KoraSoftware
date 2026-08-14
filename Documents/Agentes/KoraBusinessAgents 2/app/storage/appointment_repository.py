from datetime import datetime, timezone
import sqlite3
from typing import Any, Optional

from app.storage.sqlite import get_connection


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class AppointmentRepository:
    def create(
        self,
        *,
        clinic_id: str,
        patient_name: str,
        patient_phone: str,
        treatment_id: str,
        professional_id: str,
        resource_id: str,
        start_datetime: str,
        end_datetime: str,
        google_event_id: Optional[str],
        status: str,
    ) -> int:
        now = utc_now()

        with get_connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO appointments (
                    clinic_id,
                    patient_name,
                    patient_phone,
                    treatment_id,
                    professional_id,
                    resource_id,
                    start_datetime,
                    end_datetime,
                    google_event_id,
                    status,
                    created_at,
                    updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    clinic_id,
                    patient_name,
                    patient_phone,
                    treatment_id,
                    professional_id,
                    resource_id,
                    start_datetime,
                    end_datetime,
                    google_event_id,
                    status,
                    now,
                    now,
                ),
            )

            conn.commit()
            return int(cursor.lastrowid)

    def get_by_id(self, appointment_id: int) -> Optional[dict[str, Any]]:
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                """
                SELECT *
                FROM appointments
                WHERE id = ?
                """,
                (appointment_id,),
            )
            row = cursor.fetchone()

        return dict(row) if row else None


    def update_status(self, *, appointment_id: int, status: str) -> None:
        now = utc_now()

        with get_connection() as conn:
            conn.execute(
                """
                UPDATE appointments
                SET status = ?, updated_at = ?
                WHERE id = ?
                """,
                (status, now, appointment_id),
            )
            conn.commit()