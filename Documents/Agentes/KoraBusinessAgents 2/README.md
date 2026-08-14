# Dental Agent MVP Backend

Backend local para probar un agente-secretaría dental por WhatsApp.

Incluye:

- FastAPI
- SQLite
- Webhook WhatsApp GET/POST
- Deduplicación por `whatsapp_message_id`
- BackgroundTasks
- Lock por teléfono
- Agente por reglas, sin Claude
- Google Calendar API
- Endpoint interno para crear citas de prueba

## 1. Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/init_db.py
```

## 2. Ejecutar backend

```bash
uvicorn app.main:app --reload --port 8000
```

## 3. Probar health

```bash
curl http://localhost:8000/health
```

## 4. Probar conversación local

```bash
curl -X POST http://localhost:8000/webhook/whatsapp \
  -H "Content-Type: application/json" \
  -d '{
    "entry": [{
      "changes": [{
        "value": {
          "messages": [{
            "id": "wamid.CONV001",
            "from": "34600000000",
            "timestamp": "1710000001",
            "type": "text",
            "text": {"body": "Hola, quiero pedir cita para una limpieza dental"}
          }]
        }
      }]
    }]
  }'
```

El outbound se verá por consola si `WHATSAPP_DRY_RUN=true`.

## 5. Autorizar Google Calendar

1. Activa Google Calendar API en Google Cloud.
2. Crea credencial OAuth Client ID tipo Desktop App.
3. Descarga el JSON y guárdalo como:

```text
credentials/google_credentials.json
```

4. Ejecuta:

```bash
python scripts/google_auth.py
```

Esto generará:

```text
credentials/google_token.json
```

## 6. Crear cita real en Google Calendar

```bash
curl -X POST http://localhost:8000/internal/calendar/appointments/test-create \
  -H "Content-Type: application/json" \
  -d '{
    "patient_name": "Andrés Camacho",
    "patient_phone": "34600000000",
    "treatment_id": "cleaning",
    "professional_id": "dra_marta",
    "resource_id": "gabinete_1",
    "start_datetime": "2026-05-25T16:30:00",
    "duration_minutes": 45
  }'
```

## 7. Ver mensajes en SQLite

```bash
sqlite3 data/mvp.db
```

```sql
SELECT id, phone, direction, status, body, created_at
FROM messages
ORDER BY id ASC;
```
