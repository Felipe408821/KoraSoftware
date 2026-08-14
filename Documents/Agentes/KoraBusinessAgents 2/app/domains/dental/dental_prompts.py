from app.domains.dental.dental_config import (
    DEFAULT_ASSISTANT_NAME,
    DEFAULT_CLINIC_NAME,
    DEFAULT_DOCTOR_NAME,
    DEFAULT_CLINIC_ADDRESS,
)

WELCOME_TEMPLATE = (
    ", soy "
    f"{DEFAULT_ASSISTANT_NAME}, secretaria de la {DEFAULT_CLINIC_NAME} "
    f"de la {DEFAULT_DOCTOR_NAME}. Encantada de atenderle \n"
)

ADDRESS_TEMPLATE = (
    f"La {DEFAULT_CLINIC_NAME} de la {DEFAULT_DOCTOR_NAME} se encuentra ubicada en el {DEFAULT_CLINIC_ADDRESS} \n"
)

OPENING_HOURS_TEMPLATE = (
    f"Nuestro horario de atención es de lunes a viernes de 9:00 a 17:00 "
    f"y sábados de 9:00 a 14:00.\n"
    f"¿Quieres que te ayude a pedir, cambiar o cancelar una cita?"
)

