from typing import Any

import httpx

from app.core.config import settings


class WhatsAppClient:
    async def send_text_message(self, *, to: str, text: str) -> dict[str, Any]:
        """
        Envía un mensaje de texto por WhatsApp Cloud API.

        Si WHATSAPP_DRY_RUN=true, no envía nada real y solo imprime por consola.
        """

        normalized_to = self._normalize_phone(to)

        if settings.whatsapp_dry_run:
            print("\n================ OUTBOUND WHATSAPP ================")
            print(f"TO: {normalized_to}")
            print(f"TEXT: {text}")
            print("===================================================\n")

            return {
                "dry_run": True,
                "to": normalized_to,
                "text": text,
            }

        if not settings.whatsapp_access_token or not settings.whatsapp_phone_number_id:
            raise RuntimeError("Faltan WHATSAPP_ACCESS_TOKEN o WHATSAPP_PHONE_NUMBER_ID")

        api_version = getattr(settings, "whatsapp_api_version", "v25.0")

        url = (
            f"https://graph.facebook.com/{api_version}/"
            f"{settings.whatsapp_phone_number_id}/messages"
        )

        payload = {
            "messaging_product": "whatsapp",
            "to": normalized_to,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": text,
            },
        }

        headers = {
            "Authorization": f"Bearer {settings.whatsapp_access_token}",
            "Content-Type": "application/json",
        }

        async with httpx.AsyncClient(timeout=15) as client:
            try:
                response = await client.post(url, json=payload, headers=headers)
                response.raise_for_status()
                return response.json()

            except httpx.HTTPStatusError as exc:
                error_body = exc.response.text
                raise RuntimeError(
                    f"Error enviando WhatsApp. "
                    f"Status={exc.response.status_code}. "
                    f"Body={error_body}"
                ) from exc

    def _normalize_phone(self, phone: str) -> str:
        """
        WhatsApp Cloud API espera el número en formato internacional sin '+'.
        Ejemplo: 34600000000
        """
        return phone.replace("+", "").replace(" ", "").strip()