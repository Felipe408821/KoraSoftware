import hmac
import hashlib
from typing import Optional

from app.core.config import settings


def verify_meta_signature(raw_body: bytes, signature_header: Optional[str]) -> bool:
    # MVP local: si no hay APP_SECRET configurado, no bloqueamos.
    # En producción, añade APP_SECRET y valida X-Hub-Signature-256.
    app_secret = ""
    if not app_secret:
        return True

    if not signature_header:
        return False

    expected = "sha256=" + hmac.new(
        app_secret.encode("utf-8"),
        raw_body,
        hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(expected, signature_header)
