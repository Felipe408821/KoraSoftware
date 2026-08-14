from typing import Any

from app.agent.states import ConversationStage


def initial_state(phone: str, clinic_id: str = "clinic_demo") -> dict[str, Any]:
    return {
        "phone": phone,
        "clinic_id": clinic_id,
        "current_intent": None,
        "stage": ConversationStage.IDLE.value,
        "service_id": None,
        "preferred_date": None,
        "preferred_period": None,
        "offered_slots": [],
        "selected_slot": None,
        "patient_name": None,
        "appointment_id": None,
        "google_event_id": None,
        "appointment_status": None,
        "pending_action": None,
        "is_first_message": True,
    }
