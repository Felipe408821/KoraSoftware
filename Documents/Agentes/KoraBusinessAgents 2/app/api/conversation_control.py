from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.storage.conversation_repository import ConversationRepository


router = APIRouter(
    prefix="/internal/conversations",
    tags=["conversation-control"],
)


class TakeoverRequest(BaseModel):
    assigned_to: str | None = None
    reason: str = "manual_takeover"


class PauseRequest(BaseModel):
    duration_minutes: int | None = Field(
        default=None,
        description="Si viene vacío o null, la pausa es indefinida.",
    )
    reason: str = "manual_pause"


class CloseRequest(BaseModel):
    reason: str = "manual_close"


class ConversationControlResponse(BaseModel):
    phone: str
    mode: str
    status: str
    paused_until: str | None = None
    assigned_to: str | None = None
    handoff_reason: str | None = None


def _get_conversation_or_404(
    repo: ConversationRepository,
    phone: str,
) -> dict:
    conversation = repo.get_conversation_by_phone(phone=phone)

    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return conversation


def _to_response(conversation: dict) -> ConversationControlResponse:
    return ConversationControlResponse(
        phone=conversation["phone"],
        mode=conversation["mode"],
        status=conversation["status"],
        paused_until=conversation["paused_until"],
        assigned_to=conversation["assigned_to"],
        handoff_reason=conversation["handoff_reason"],
    )


@router.get("/{phone}", response_model=ConversationControlResponse)
def get_conversation_control(phone: str):
    repo = ConversationRepository()
    conversation = _get_conversation_or_404(repo, phone)
    return _to_response(conversation)


@router.post("/{phone}/takeover", response_model=ConversationControlResponse)
def takeover_conversation(
    phone: str,
    body: TakeoverRequest,
):
    repo = ConversationRepository()

    _get_conversation_or_404(repo, phone)

    repo.mark_pending_human(
        phone=phone,
        reason=body.reason,
        assigned_to=body.assigned_to,
    )

    conversation = _get_conversation_or_404(repo, phone)
    return _to_response(conversation)


@router.post("/{phone}/release", response_model=ConversationControlResponse)
def release_conversation_to_bot(phone: str):
    repo = ConversationRepository()

    _get_conversation_or_404(repo, phone)

    repo.release_to_bot(phone=phone)

    conversation = _get_conversation_or_404(repo, phone)
    return _to_response(conversation)


@router.post("/{phone}/pause", response_model=ConversationControlResponse)
def pause_conversation(
    phone: str,
    body: PauseRequest,
):
    repo = ConversationRepository()

    _get_conversation_or_404(repo, phone)

    paused_until = None

    if body.duration_minutes is not None:
        paused_until = (
            datetime.now(timezone.utc) + timedelta(minutes=body.duration_minutes)
        ).isoformat()

    repo.pause_conversation(
        phone=phone,
        paused_until=paused_until,
        reason=body.reason,
    )

    conversation = _get_conversation_or_404(repo, phone)
    return _to_response(conversation)


@router.post("/{phone}/close", response_model=ConversationControlResponse)
def close_conversation(
    phone: str,
    body: CloseRequest,
):
    repo = ConversationRepository()

    _get_conversation_or_404(repo, phone)

    repo.close_conversation(
        phone=phone,
        reason=body.reason,
    )

    conversation = _get_conversation_or_404(repo, phone)
    return _to_response(conversation)