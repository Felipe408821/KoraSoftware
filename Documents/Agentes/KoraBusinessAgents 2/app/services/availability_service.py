"""Compatibility wrapper.

The availability business logic now lives in app.domains.appointments.
Keep this module so older imports continue working during the refactor.
"""

from app.domains.appointments.availability_service import AvailabilityService

__all__ = ["AvailabilityService"]
