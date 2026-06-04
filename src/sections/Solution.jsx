import Section from '../components/Section.jsx'
import Reveal from '../components/Reveal.jsx'
import { IconCheck } from '../components/icons.jsx'

const capabilities = [
  'Responder preguntas frecuentes al instante',
  'Agendar citas según tu disponibilidad',
  'Cancelar o modificar citas existentes',
  'Consultar huecos y disponibilidad real',
  'Recoger los datos básicos del cliente',
  'Escalar a una persona cuando hace falta',
]

export default function Solution() {
  return (
    <Section id="solucion" className="bg-[#fafafe]">
      <div className="grid items-center gap-12 lg:grid-cols-2">
        <Reveal>
          <span className="eyebrow">La solución</span>
          <h2 className="mt-5 text-3xl font-bold tracking-tight text-ink sm:text-4xl md:text-[2.6rem] md:leading-[1.1]">
            Kora actúa como una recepcionista digital inteligente
          </h2>
          <p className="mt-5 text-lg leading-relaxed text-ink-muted">
            Un agente conversacional que entiende a tus clientes, conoce las
            reglas de tu negocio y gestiona las conversaciones de principio a
            fin, sin perder el tono humano y derivando a tu equipo cuando es
            necesario.
          </p>
        </Reveal>

        <Reveal delay={120}>
          <div className="card-ring p-2">
            <ul className="divide-y divide-ink/5">
              {capabilities.map((c) => (
                <li key={c} className="flex items-center gap-3.5 px-4 py-3.5">
                  <span className="grid h-7 w-7 shrink-0 place-items-center rounded-full bg-brand-gradient text-white shadow-sm">
                    <IconCheck width={15} height={15} />
                  </span>
                  <span className="text-[15px] font-medium text-ink-soft">{c}</span>
                </li>
              ))}
            </ul>
          </div>
        </Reveal>
      </div>
    </Section>
  )
}
