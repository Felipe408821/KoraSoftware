from app.agent.orchestrator import DentalAgent
from app.core.conversation_locks import get_phone_lock
from app.integrations.whatsapp.client import WhatsAppClient
from app.services.conversation_control_service import (
    ControlAction,
    ConversationControlService,
)
from app.storage.conversation_repository import ConversationRepository
from app.storage.message_repository import MessageRepository


class MessageProcessor:
    """Processes accepted inbound messages outside the webhook request.

    The webhook only persists the inbound message and returns 200 OK.
    This processor owns the slower work: conversation state, agent execution,
    outbound WhatsApp delivery and final message status.
    """

    def __init__(self) -> None:
        self.message_repo = MessageRepository()
        self.conversation_repo = ConversationRepository()
        self.agent = DentalAgent()
        self.whatsapp_client = WhatsAppClient()
        self.conversation_control_service = ConversationControlService()

    async def process(self, *, whatsapp_message_id: str, phone: str, text: str) -> None:
        lock = get_phone_lock(phone)

        async with lock:
            reply_to_send: str | None = None

            try:
                self.message_repo.mark_processing(whatsapp_message_id)

                state = self.conversation_repo.get_or_create_state(phone=phone)

                self.conversation_repo.touch_last_message(
                    phone=phone,
                    preview=text,
                )

                conversation = self.conversation_repo.get_conversation_by_phone(
                    phone=phone,
                )

                if conversation is None:
                    raise RuntimeError(
                        f"Conversation not found after get_or_create_state: {phone}"
                    )

                decision = self.conversation_control_service.decide_for_inbound_message(
                    conversation=conversation,
                    text=text,
                )

                if decision.action == ControlAction.DO_NOTHING:
                    self.message_repo.mark_processed(whatsapp_message_id)
                    return

                if decision.action == ControlAction.HANDOFF_TO_HUMAN:
                    self.conversation_repo.mark_pending_human(
                        phone=phone,
                        reason=decision.reason,
                    )

                    if decision.should_send_handoff_message and decision.handoff_message:
                        reply_to_send = decision.handoff_message

                        await self.whatsapp_client.send_text_message(
                            to=phone,
                            text=reply_to_send,
                        )

                        self.message_repo.insert_outbound(
                            phone=phone,
                            body=reply_to_send,
                            status="sent",
                        )

                    self.message_repo.mark_processed(whatsapp_message_id)
                    return

                result = await self.agent.run(
                    phone=phone,
                    user_text=text,
                    state=state,
                )

                reply_to_send = result.reply

                self.conversation_repo.save_state(
                    phone=phone,
                    state=result.new_state,
                    clinic_id=result.new_state.get("clinic_id", "clinic_demo"),
                )

                if not reply_to_send:
                    self.message_repo.mark_processed(whatsapp_message_id)
                    return

                refreshed_conversation = self.conversation_repo.get_conversation_by_phone(
                    phone=phone,
                )

                if refreshed_conversation is None:
                    raise RuntimeError(f"Conversation not found before send: {phone}")

                can_still_send = (
                    self.conversation_control_service
                    .should_send_bot_response_before_delivery(
                        conversation=refreshed_conversation,
                    )
                )

                if not can_still_send:
                    self.message_repo.insert_outbound(
                        phone=phone,
                        body=reply_to_send,
                        status="cancelled_control_changed",
                    )
                    self.message_repo.mark_processed(whatsapp_message_id)
                    return

                await self.whatsapp_client.send_text_message(
                    to=phone,
                    text=reply_to_send,
                )

                self.message_repo.insert_outbound(
                    phone=phone,
                    body=reply_to_send,
                    status="sent",
                )

                self.message_repo.mark_processed(whatsapp_message_id)

            except Exception as exc:
                if reply_to_send:
                    self.message_repo.insert_outbound(
                        phone=phone,
                        body=reply_to_send,
                        status="failed",
                    )

                self.message_repo.mark_failed(whatsapp_message_id)
                print(f"ERROR procesando mensaje {whatsapp_message_id}: {exc}")