import Section from '../components/Section.jsx'
import Reveal from '../components/Reveal.jsx'
import {
  IconStethoscope,
  IconSparkle,
  IconBuilding,
  IconBriefcase,
  IconBook,
  IconWrench,
} from '../components/icons.jsx'

const sectors = [
  { icon: <IconStethoscope width={22} height={22} />, title: 'Clínicas médicas' },
  { icon: <IconSparkle width={22} height={22} />, title: 'Centros estéticos' },
  { icon: <IconBuilding width={22} height={22} />, title: 'Inmobiliarias' },
  { icon: <IconBriefcase width={22} height={22} />, title: 'Despachos profesionales' },
  { icon: <IconBook width={22} height={22} />, title: 'Academias' },
  { icon: <IconWrench width={22} height={22} />, title: 'Talleres y servicios locales' },
]

export default function FutureUseCases() {
  return (
    <Section
      className="bg-[#fafafe]"
      eyebrow="Casos de uso futuros"
      title="Una misma tecnología, muchos sectores"
      subtitle="Cualquier negocio que gestione clientes, citas o consultas frecuentes puede apoyarse en Kora."
    >
      <div className="mt-14 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        {sectors.map((s, i) => (
          <Reveal key={s.title} delay={i * 60}>
            <div className="group flex items-center gap-4 rounded-3xl border border-ink/5 bg-white p-5 shadow-soft transition-all duration-300 hover:-translate-y-1 hover:shadow-card">
              <span className="inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-brand-gradient-soft text-brand-600 ring-1 ring-brand-100">
                {s.icon}
              </span>
              <span className="text-base font-semibold text-ink">{s.title}</span>
            </div>
          </Reveal>
        ))}
      </div>
    </Section>
  )
}
