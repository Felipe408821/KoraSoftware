AFFIRMATIONS = {
    "sí", "si", "confirmo", "vale", "ok", "perfecto", "claro",
    "dale", "por supuesto", "exacto", "correcto", "venga", "adelante",
    "de acuerdo", "listo", "sip", "yes", "obvio", "genial", "bien",
}

NEGATIONS = {
    "no", "nope", "para nada", "mejor no", "mantener", "déjala",
    "dejala", "no me interesa", "cambiar", "otra", "mejor", "negativo",
    "cancela", "olvídalo", "olvidalo",
}

RESTART_KEYWORDS = {
    "reiniciar", "empezar de nuevo", "menú", "menu", "inicio",
    "volver", "reset", "otra cosa",
}

CANCEL_KEYWORDS = {
    "cancelar", "anular", "eliminar", "borrar", "quitar la cita",
    "cancelar cita", "anular cita", "borrala", "elimínala", "eliminala",
    "no la quiero", "quitar cita",
}

GREETING_KEYWORDS = {
    "hola", "buenas", "buenos días", "buenos dias", "buenas tardes",
    "buenas noches", "hey", "ey", "saludos", "hello",
}

BOOKING_KEYWORDS = {
    "cita", "reservar", "agenda", "agendar", "quiero", "necesito",
    "pedir cita", "solicitar", "apuntar", "reserva",
}

URGENT_KEYWORDS = {
    "urgente", "dolor fuerte", "sangrado", "infección", "infeccion",
    "fiebre", "no puedo respirar", "emergencia", "diagnóstico",
    "diagnostico", "receta", "medicación", "medicacion",
}


def normalize(text: str) -> str:
    return text.lower().strip()


def is_affirmation(text: str) -> bool:
    return any(word in text.split() or text == word for word in AFFIRMATIONS)


def is_negation(text: str) -> bool:
    return any(word in text.split() or text == word for word in NEGATIONS)


def wants_restart(text: str) -> bool:
    return any(keyword in text for keyword in RESTART_KEYWORDS)


def wants_to_cancel(text: str) -> bool:
    return any(keyword in text for keyword in CANCEL_KEYWORDS)


def is_greeting(text: str) -> bool:
    return any(keyword in text for keyword in GREETING_KEYWORDS)


def wants_booking(text: str) -> bool:
    return any(keyword in text for keyword in BOOKING_KEYWORDS)


def needs_human_handoff(text: str) -> bool:
    return any(keyword in text for keyword in URGENT_KEYWORDS)
