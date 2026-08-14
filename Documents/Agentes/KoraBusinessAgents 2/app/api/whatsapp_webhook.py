from typing import Optional

from fastapi import APIRouter, BackgroundTasks, HTTPException, Query, Request
from fastapi.responses import PlainTextResponse

from app.core.config import settings
from app.integrations.whatsapp.parser import parse_incoming_text_message
from app.jobs.message_processor import MessageProcessor
from app.storage.message_repository import MessageRepository


router = APIRouter(prefix="/webhook", tags=["whatsapp-webhook"])


@router.get("/whatsapp")
def verify_webhook(
    hub_mode: Optional[str] = Query(default=None, alias="hub.mode"),
    hub_verify_token: Optional[str] = Query(default=None, alias="hub.verify_token"),
    hub_challenge: Optional[str] = Query(default=None, alias="hub.challenge"),
):
    if hub_mode == "subscribe" and hub_verify_token == settings.whatsapp_verify_token:
        return PlainTextResponse(content=hub_challenge or "")

    raise HTTPException(status_code=403, detail="Invalid verify token")


@router.post("/whatsapp")
async def receive_webhook(request: Request, background_tasks: BackgroundTasks) -> dict[str, str]:
    payload = await request.json()

    parsed = parse_incoming_text_message(payload)
    if parsed is None:
        return {"status": "ignored"}

    message_repo = MessageRepository()

    is_new = message_repo.insert_inbound_if_new(
        whatsapp_message_id=parsed.message_id,
        phone=parsed.phone,
        body=parsed.text,
    )

    if not is_new:
        return {"status": "duplicate_ignored"}

    processor = MessageProcessor()

    background_tasks.add_task(
        processor.process,
        whatsapp_message_id=parsed.message_id,
        phone=parsed.phone,
        text=parsed.text,
    )

    return {"status": "accepted"}