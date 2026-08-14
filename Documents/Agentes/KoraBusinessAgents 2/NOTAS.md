https://graph.facebook.com/v25.0/1301882065411969/subscribed_apps


curl -X POST "https://graph.facebook.com/v25.0/1301882065411969/subscribed_apps" \
  -H "Authorization: Bearer EAAOKVzI5hZCMBRsONrIpwIfRpI8qTvV6SGVEPvocaVat2GIM5PXWZCTOsVYEgmdQ9UqRxXQbkDP5WgBX3FZBNl1NYjVYuxX7OPS4vIhEkDqEij8uibldvPdAbAjCnZAEoKJ1U0auquZAopRX5xkjyNLyiS9YEw1C5HhgWI6FguqiF3betEiIIeJ1OFVbUJ1SAGYRShSAe61R2W0W7xyOHtF1BrNVlAYb5biXC8DuBtz3mrZCy7WYc26nGaP4PMxIXUaZCQ2GftKDEdI6Co1oj8sa0bP" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "subscribed_fields=messages"


  curl -X GET "https://graph.facebook.com/v25.0/1301882065411969/subscribed_apps" \
  -H "Authorization: Bearer EAAOKVzI5hZCMBRsONrIpwIfRpI8qTvV6SGVEPvocaVat2GIM5PXWZCTOsVYEgmdQ9UqRxXQbkDP5WgBX3FZBNl1NYjVYuxX7OPS4vIhEkDqEij8uibldvPdAbAjCnZAEoKJ1U0auquZAopRX5xkjyNLyiS9YEw1C5HhgWI6FguqiF3betEiIIeJ1OFVbUJ1SAGYRShSAe61R2W0W7xyOHtF1BrNVlAYb5biXC8DuBtz3mrZCy7WYc26nGaP4PMxIXUaZCQ2GftKDEdI6Co1oj8sa0bP" 

  Te voy a compartir mi codigo ConversationRepository, para que me lo devuelvas con las adaptaciones concretas sobre el:


  curl -X POST "http://localhost:8000/internal/conversations/34699000001/takeover" \
  -H "Content-Type: application/json" \
  -d '{
    "assigned_to": "recepcionista_1",
    "reason": "manual_takeover"
  }'