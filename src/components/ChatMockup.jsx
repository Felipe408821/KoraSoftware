// Mockup de conversación inspirado en apps de mensajería.
// NO usa el logo ni los colores de marca de WhatsApp: usa la identidad de Kora.
// Muestra a un paciente pidiendo cita y a Kora consultando disponibilidad
// y confirmando.

function Bubble({ from, children, time }) {
  const isUser = from === 'user'
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`relative max-w-[78%] rounded-2xl px-3.5 py-2.5 text-[13.5px] leading-relaxed shadow-sm ${
          isUser
            ? 'rounded-br-md bg-brand-gradient text-white'
            : 'rounded-bl-md bg-white text-ink ring-1 ring-ink/5'
        }`}
      >
        {children}
        {time && (
          <span
            className={`mt-1 block text-[10px] ${
              isUser ? 'text-white/70' : 'text-ink-muted'
            }`}
          >
            {time}
          </span>
        )}
      </div>
    </div>
  )
}

export default function ChatMockup() {
  return (
    <div className="relative mx-auto w-full max-w-sm">
      {/* Halo de gradiente detrás del teléfono */}
      <div
        aria-hidden="true"
        className="absolute -inset-6 -z-10 rounded-[3rem] bg-brand-gradient opacity-20 blur-3xl"
      />

      <div className="overflow-hidden rounded-[2.2rem] border border-ink/10 bg-[#eef1f8] shadow-glow">
        {/* Barra superior del chat */}
        <div className="flex items-center gap-3 bg-white px-4 py-3.5">
          <span className="grid h-9 w-9 place-items-center rounded-full bg-brand-gradient text-white">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
              <circle cx="12" cy="12" r="7" stroke="white" strokeWidth="2" />
              <circle cx="12" cy="12" r="2.4" fill="white" />
            </svg>
          </span>
          <div className="flex-1">
            <p className="text-sm font-semibold text-ink">Kora · Clínica Dental Sonríe</p>
            <p className="flex items-center gap-1.5 text-[11px] text-emerald-600">
              <span className="h-1.5 w-1.5 rounded-full bg-emerald-500" />
              en línea · responde al instante
            </p>
          </div>
          <span className="text-xs font-medium text-brand-600">24/7</span>
        </div>

        {/* Conversación */}
        <div className="space-y-2.5 px-4 py-5">
          <Bubble from="user" time="09:41">
            Hola, quería pedir cita para una limpieza dental 🦷
          </Bubble>

          <Bubble from="kora">
            ¡Hola! Claro 😊 ¿Prefieres mañana por la mañana o por la tarde?
          </Bubble>

          <Bubble from="user" time="09:41">
            Por la tarde mejor
          </Bubble>

          {/* Indicador "consultando" */}
          <div className="flex justify-start">
            <div className="flex items-center gap-2 rounded-2xl rounded-bl-md bg-white px-3 py-2 text-[11px] text-ink-muted ring-1 ring-ink/5">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" className="text-brand-500">
                <rect x="3" y="4.5" width="18" height="16" rx="2.5" />
                <path d="M3 9h18M8 3v3M16 3v3" />
              </svg>
              Consultando disponibilidad…
            </div>
          </div>

          <Bubble from="kora">
            Tengo un hueco el <strong>jueves a las 17:30</strong> con la Dra. Pérez. ¿Te
            lo reservo?
          </Bubble>

          <Bubble from="user" time="09:42">
            Perfecto, sí 👍
          </Bubble>

          <Bubble from="kora" time="09:42">
            ✅ Cita confirmada — jueves 17:30. Te enviaré un recordatorio el día
            anterior. ¡Hasta entonces!
          </Bubble>
        </div>

        {/* Barra de entrada (decorativa) */}
        <div className="flex items-center gap-2 border-t border-ink/5 bg-white px-4 py-3">
          <div className="flex-1 rounded-full bg-[#eef1f8] px-4 py-2 text-[13px] text-ink-muted">
            Escribe un mensaje…
          </div>
          <span className="grid h-9 w-9 place-items-center rounded-full bg-brand-gradient text-white">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M5 12h14M13 6l6 6-6 6" />
            </svg>
          </span>
        </div>
      </div>
    </div>
  )
}
