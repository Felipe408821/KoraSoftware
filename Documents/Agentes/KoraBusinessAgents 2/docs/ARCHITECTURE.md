# Kora Business Agents — arquitectura refactorizada

## Objetivo

El proyecto deja de depender de un único `dental_agent.py` grande y pasa a una estructura preparada para crecer a más verticales de negocio.

## Flujo principal

```text
WhatsApp / Meta
  ↓
app/api/whatsapp_webhook.py
  ↓ guarda mensaje y responde 200 OK
app/jobs/message_processor.py
  ↓
app/agent/orchestrator.py
  ↓
app/domains/appointments/*
  ↓
app/integrations/calendar/*
  ↓
Google Calendar
```

## Capas

- `app/api`: endpoints HTTP.
- `app/jobs`: procesamiento asíncrono/background.
- `app/agent`: orquestación conversacional, estados e intención.
- `app/domains`: lógica de negocio por dominio.
- `app/integrations`: proveedores externos.
- `app/storage`: persistencia SQLite.
- `app/services`: wrappers de compatibilidad temporal.

## Decisión clave

El agente ya no debe llamar por HTTP a endpoints internos del mismo backend. El endpoint interno y el agente comparten la misma lógica de dominio:

```text
AgentOrchestrator ─┐
                   ├─ AppointmentService → CalendarProvider
Internal API ──────┘
```

## Compatibilidad

Se mantienen wrappers para no romper imports existentes:

- `app/agents/dental_agent.py`
- `app/services/appointment_service.py`
- `app/services/availability_service.py`
- `app/services/message_processor.py`
