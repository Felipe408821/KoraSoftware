import Section from '../components/Section.jsx'
import Reveal from '../components/Reveal.jsx'
import { IconTooth, IconCheck } from '../components/icons.jsx'

const examples = [
  'Limpiezas y revisiones periódicas',
  'Ortodoncia y tratamientos',
  'Urgencias dentales',
  'Confirmación y recordatorio de citas',
  'Horarios, ubicación y cómo llegar',
  'Precios orientativos de servicios',
]

export default function UseCaseDental() {
  return (
    <Section id="casos-de-uso">
      <div className="grid items-center gap-12 lg:grid-cols-2">
        <Reveal>
          <span className="eyebrow">
            <IconTooth width={14} height={14} />
            Caso de uso inicial
          </span>
          <h2 className="mt-5 text-3xl font-bold tracking-tight text-ink sm:text-4xl md:text-[2.4rem] md:leading-[1.12]">
            Empezamos por clínicas dentales, pero la tecnología escala a
            cualquier negocio de servicios
          </h2>
          <p className="mt-5 text-lg leading-relaxed text-ink-muted">
            Kora gestiona las consultas más habituales de una clínica dental,
            desde la primera duda hasta la cita confirmada, integrándose en la
            forma de trabajar de tu equipo.
          </p>
        </Reveal>

        <Reveal delay={120}>
          <div className="grid gap-3 sm:grid-cols-2">
            {examples.map((e) => (
              <div
                key={e}
                className="flex items-start gap-3 rounded-2xl border border-ink/5 bg-white p-4 shadow-soft"
              >
                <span className="mt-0.5 grid h-6 w-6 shrink-0 place-items-center rounded-full bg-brand-50 text-brand-600">
                  <IconCheck width={14} height={14} />
                </span>
                <span className="text-sm font-medium text-ink-soft">{e}</span>
              </div>
            ))}
          </div>
        </Reveal>
      </div>
    </Section>
  )
}
