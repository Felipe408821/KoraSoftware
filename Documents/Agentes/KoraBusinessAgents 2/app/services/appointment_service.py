"""Compatibility wrapper.

The appointment business logic now lives in app.domains.appointments.
Keep this module so older imports continue working during the refactor.
"""

from app.domains.appointments.appointment_service import AppointmentService

__all__ = ["AppointmentService"]
