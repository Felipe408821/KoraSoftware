from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.whatsapp_webhook import router as whatsapp_webhook_router
from app.api.calendar_internal import router as calendar_internal_router
from app.api.conversation_control import router as conversation_control_router


app = FastAPI(title="Dental Agent MVP")

app.include_router(health_router)
app.include_router(whatsapp_webhook_router)
app.include_router(calendar_internal_router)
app.include_router(conversation_control_router)