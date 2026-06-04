import Button from '../components/Button.jsx'
import ChatMockup from '../components/ChatMockup.jsx'
import Reveal from '../components/Reveal.jsx'
import { demoMailto } from '../config/site.js'
import { IconArrowRight, IconCheck } from '../components/icons.jsx'

const pills = ['Atención 24/7', 'Gestión de citas', 'Respuestas al instante']

export default function Hero() {
  return (
    <section className="relative overflow-hidden">
      {/* Fondo decorativo: gradiente sutil + grid */}
      <div aria-hidden="true" className="pointer-events-none absolute inset-0 -z-10">
        <div className="absolute inset-x-0 top-0 h-[42rem] bg-gradient-to-b from-brand-50/80 via-white to-white" />
        <div className="absolute -right-24 top-10 h-72 w-72 rounded-full bg-violetx-400/20 blur-3xl" />
        <div className="absolute -left-24 top-32 h-72 w-72 rounded-full bg-cyanx-400/20 blur-3xl" />
      </div>

      <div className="container-kora grid items-center gap-14 py-16 sm:py-24 lg:grid-cols-2 lg:gap-10">
        {/* Columna de texto */}
        <div>
          <Reveal>
            <span className="eyebrow">
              <span className="h-1.5 w-1.5 rounded-full bg-brand-gradient" />
              KoraBusinessAgents · Agentes de IA
            </span>
          </Reveal>

          <Reveal delay={80}>
            <h1 className="mt-6 text-4xl font-bold leading-[1.08] tracking-tight text-ink sm:text-5xl md:text-[3.4rem]">
              Agentes de IA para automatizar la atención de tu negocio por{' '}
              <span className="text-gradient">WhatsApp</span>
            </h1>
          </Reveal>

          <Reveal delay={160}>
            <p className="mt-6 max-w-xl text-lg leading-relaxed text-ink-muted">
              Kora Software ayuda a clínicas y negocios de servicios a responder
              clientes, gestionar citas y reducir tareas administrativas con
              agentes inteligentes disponibles 24/7.
            </p>
          </Reveal>

          <Reveal delay={240}>
            <div className="mt-8 flex flex-col gap-3 sm:flex-row">
              <Button href={demoMailto} size="lg">
                Solicitar demo
                <IconArrowRight width={18} height={18} />
              </Button>
              <Button href="#como-funciona" variant="secondary" size="lg">
                Ver cómo funciona
              </Button>
            </div>
          </Reveal>

          <Reveal delay={320}>
            <ul className="mt-8 flex flex-wrap gap-x-6 gap-y-2">
              {pills.map((p) => (
                <li key={p} className="flex items-center gap-2 text-sm font-medium text-ink-soft">
                  <span className="grid h-5 w-5 place-items-center rounded-full bg-brand-50 text-brand-600">
                    <IconCheck width={14} height={14} />
                  </span>
                  {p}
                </li>
              ))}
            </ul>
          </Reveal>
        </div>

        {/* Columna del mockup */}
        <Reveal delay={200} className="lg:pl-6">
          <div className="animate-float">
            <ChatMockup />
          </div>
        </Reveal>
      </div>
    </section>
  )
}
