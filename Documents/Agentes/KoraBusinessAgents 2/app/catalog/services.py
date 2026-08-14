from dataclasses import dataclass, field


@dataclass(frozen=True)
class ServiceDefinition:
    service_id: str
    label: str                   # texto que se muestra al paciente
    duration_minutes: int
    professional_id: str
    resource_id: str
    keywords: list[str] = field(default_factory=list)


SERVICE_CATALOG: dict[str, ServiceDefinition] = {
    "cleaning": ServiceDefinition(
        service_id="cleaning",
        label="limpieza dental",
        duration_minutes=45,
        professional_id="Dra María Fernanda Valdivieso",
        resource_id="gabinete_1",
        keywords=["limpieza", "limpieza dental", "higiene", "higiene dental"],
    ),
    "orthodontics_review": ServiceDefinition(
        service_id="orthodontics_review",
        label="revisión de ortodoncia",
        duration_minutes=30,
        professional_id="dr_pedro",
        resource_id="gabinete_2",
        keywords=["ortodoncia", "brackets", "revisión ortodoncia", "revision ortodoncia"],
    ),
    "extraction": ServiceDefinition(
        service_id="extraction",
        label="extracción dental",
        duration_minutes=60,
        professional_id="dra_marta",
        resource_id="gabinete_1",
        keywords=["extracción", "extraccion", "sacar muela", "sacar diente", "muela del juicio"],
    ),
    "general_checkup": ServiceDefinition(
        service_id="general_checkup",
        label="revisión general",
        duration_minutes=30,
        professional_id="dra_marta",
        resource_id="gabinete_1",
        keywords=["revisión", "revision", "chequeo", "consulta general", "revisión general"],
    ),
}


def detect_service(text: str) -> ServiceDefinition | None:
    """
    Detecta el servicio mencionado en el texto del usuario.
    Recorre el catálogo en orden y devuelve el primero que coincida.
    Devuelve None si no hay coincidencia.
    """
    text_lower = text.lower()
    for service in SERVICE_CATALOG.values():
        if any(kw in text_lower for kw in service.keywords):
            return service
    return None


def get_service(service_id: str) -> ServiceDefinition | None:
    """Devuelve un ServiceDefinition por su ID, o None si no existe."""
    return SERVICE_CATALOG.get(service_id)


def list_services_text() -> str:
    """Devuelve un texto con los servicios disponibles para mostrar al paciente."""
    return "\n".join(f"• {s.label}" for s in SERVICE_CATALOG.values())