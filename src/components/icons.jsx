// Set de iconos SVG (estilo línea, stroke 1.7). Limpios y coherentes.
// Heredan el color con currentColor y aceptan className.

const base = {
  width: 22,
  height: 22,
  viewBox: '0 0 24 24',
  fill: 'none',
  stroke: 'currentColor',
  strokeWidth: 1.7,
  strokeLinecap: 'round',
  strokeLinejoin: 'round',
}

export const IconClock = (p) => (
  <svg {...base} {...p}>
    <circle cx="12" cy="12" r="9" />
    <path d="M12 7v5l3 2" />
  </svg>
)

export const IconCalendar = (p) => (
  <svg {...base} {...p}>
    <rect x="3" y="4.5" width="18" height="16" rx="2.5" />
    <path d="M3 9h18M8 3v3M16 3v3" />
    <path d="M8.5 14h.01M12 14h.01M15.5 14h.01" />
  </svg>
)

export const IconChat = (p) => (
  <svg {...base} {...p}>
    <path d="M21 12a8 8 0 0 1-11.5 7.2L4 21l1.8-5.5A8 8 0 1 1 21 12Z" />
    <path d="M8.5 11h7M8.5 14h4" />
  </svg>
)

export const IconSparkle = (p) => (
  <svg {...base} {...p}>
    <path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9L12 3Z" />
    <path d="M19 15l.7 1.8L21.5 17.5l-1.8.7L19 20l-.7-1.8L16.5 17.5l1.8-.7L19 15Z" />
  </svg>
)

export const IconChart = (p) => (
  <svg {...base} {...p}>
    <path d="M4 20V4M4 20h16" />
    <path d="M8 16v-3M12 16V9M16 16v-6M20 16v-9" />
  </svg>
)

export const IconUsers = (p) => (
  <svg {...base} {...p}>
    <circle cx="9" cy="8" r="3.2" />
    <path d="M3.5 19a5.5 5.5 0 0 1 11 0" />
    <path d="M16 5.2a3.2 3.2 0 0 1 0 5.6M17.5 19a5.5 5.5 0 0 0-3-4.9" />
  </svg>
)

export const IconShield = (p) => (
  <svg {...base} {...p}>
    <path d="M12 3l7 3v5c0 4.5-3 7.8-7 9-4-1.2-7-4.5-7-9V6l7-3Z" />
    <path d="M9 12l2 2 4-4" />
  </svg>
)

export const IconLayers = (p) => (
  <svg {...base} {...p}>
    <path d="M12 3l8 4.5-8 4.5-8-4.5L12 3Z" />
    <path d="M4 12l8 4.5L20 12M4 16.5l8 4.5 8-4.5" />
  </svg>
)

export const IconRefresh = (p) => (
  <svg {...base} {...p}>
    <path d="M20 11a8 8 0 0 0-14-4.5L4 8" />
    <path d="M4 4v4h4" />
    <path d="M4 13a8 8 0 0 0 14 4.5L20 16" />
    <path d="M20 20v-4h-4" />
  </svg>
)

export const IconTooth = (p) => (
  <svg {...base} {...p}>
    <path d="M7.5 3.5C5.5 3.5 4 5.2 4 7.4c0 1.7.6 2.8.9 4.4.3 1.6.2 3 .7 5.1.3 1.4.6 3.1 1.7 3.1 1.3 0 1.2-2.4 2-4 .4-.8.8-1.3 1.7-1.3s1.3.5 1.7 1.3c.8 1.6.7 4 2 4 1.1 0 1.4-1.7 1.7-3.1.5-2.1.4-3.5.7-5.1.3-1.6.9-2.7.9-4.4 0-2.2-1.5-3.9-3.5-3.9-1.5 0-2.3.8-3.5.8s-2-.8-3.5-.8Z" />
  </svg>
)

export const IconStethoscope = (p) => (
  <svg {...base} {...p}>
    <path d="M5 3v5a4 4 0 0 0 8 0V3" />
    <path d="M5 3H3.5M13 3h1.5" />
    <path d="M9 16v1a4 4 0 0 0 8 0v-2" />
    <circle cx="18" cy="12" r="2.2" />
  </svg>
)

export const IconBuilding = (p) => (
  <svg {...base} {...p}>
    <path d="M4 21V6l8-3 8 3v15" />
    <path d="M4 21h16" />
    <path d="M9 9h.01M15 9h.01M9 13h.01M15 13h.01M9 17h.01M15 17h.01" />
  </svg>
)

export const IconBriefcase = (p) => (
  <svg {...base} {...p}>
    <rect x="3" y="7.5" width="18" height="12" rx="2.5" />
    <path d="M9 7.5V6a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v1.5M3 12.5h18" />
  </svg>
)

export const IconBook = (p) => (
  <svg {...base} {...p}>
    <path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5V5.5Z" />
    <path d="M4 20.5A2.5 2.5 0 0 1 6.5 18H20" />
  </svg>
)

export const IconWrench = (p) => (
  <svg {...base} {...p}>
    <path d="M14.5 6a3.5 3.5 0 0 0-4.6 4.3L4 16.2 6.8 19l5.9-5.9A3.5 3.5 0 0 0 17 8.5l-2.2 2.2-1.5-1.5L15.5 7" />
  </svg>
)

export const IconArrowRight = (p) => (
  <svg {...base} {...p}>
    <path d="M5 12h14M13 6l6 6-6 6" />
  </svg>
)

export const IconCheck = (p) => (
  <svg {...base} {...p}>
    <path d="M5 12.5l4.5 4.5L19 7" />
  </svg>
)

export const IconAlert = (p) => (
  <svg {...base} {...p}>
    <path d="M12 3l9 16H3l9-16Z" />
    <path d="M12 9v4M12 16h.01" />
  </svg>
)

export const IconLock = (p) => (
  <svg {...base} {...p}>
    <rect x="5" y="11" width="14" height="9" rx="2.5" />
    <path d="M8 11V8a4 4 0 0 1 8 0v3M12 15v2" />
  </svg>
)

export const IconRoute = (p) => (
  <svg {...base} {...p}>
    <circle cx="6" cy="18" r="2.4" />
    <circle cx="18" cy="6" r="2.4" />
    <path d="M8.4 18H14a3.5 3.5 0 0 0 0-7H10a3.5 3.5 0 0 1 0-7h5.6" />
  </svg>
)

export const IconBolt = (p) => (
  <svg {...base} {...p}>
    <path d="M13 3 4 14h6l-1 7 9-11h-6l1-7Z" />
  </svg>
)
