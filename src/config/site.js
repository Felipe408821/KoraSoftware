// =============================================================================
//  CONFIGURACIÓN CENTRAL DEL SITIO
// -----------------------------------------------------------------------------
//  Cambia aquí los datos de la empresa cuando estén disponibles
//  (email definitivo, dominio, teléfono de WhatsApp, nombre legal, etc.).
//  Todos los componentes y páginas leen de este archivo.
// =============================================================================

export const site = {
  brand: 'Kora Software',
  group: 'Kora Group',
  tagline: 'Agentes de IA para negocios de servicios.',

  // Contacto provisional — sustituir cuando se disponga del definitivo
  email: 'email@email.com',

  // Número de WhatsApp en formato internacional SIN signos ni espacios
  // (ej. 34600000000). Déjalo vacío ('') para ocultar el botón de WhatsApp.
  whatsapp: '',

  // Dominio cuando exista (sin barra final). De momento GitHub Pages.
  domain: 'https://korasoftware.ai',

  // País base inicial / jurisdicción de referencia para textos legales
  country: 'España',

  // Fecha de entrada en vigor de los documentos legales
  legalEffectiveDate: '4 de junio de 2026',
  legalEffectiveDateEn: 'June 4, 2026',

  // Año para el copyright del footer
  copyrightYear: 2026,
}

// Genera un enlace mailto con asunto y cuerpo opcionales
export function mailtoLink({ subject = '', body = '' } = {}) {
  const params = new URLSearchParams()
  if (subject) params.set('subject', subject)
  if (body) params.set('body', body)
  const qs = params.toString()
  return `mailto:${site.email}${qs ? `?${qs}` : ''}`
}

// Genera un enlace a WhatsApp con mensaje prerrellenado (si hay número)
export function whatsappLink(message = 'Hola, me gustaría solicitar una demo de Kora Software.') {
  if (!site.whatsapp) return null
  return `https://wa.me/${site.whatsapp}?text=${encodeURIComponent(message)}`
}

// Enlace por defecto para los CTA de "Solicitar demo"
export const demoMailto = mailtoLink({
  subject: 'Solicitud de demo — Kora Software',
  body:
    'Hola, me gustaría solicitar una demo de KoraBusinessAgents.\n\n' +
    'Nombre:\n' +
    'Empresa / clínica:\n' +
    'Email:\n' +
    'Teléfono:\n' +
    'Sector:\n' +
    '¿Qué te gustaría automatizar?:\n',
})
