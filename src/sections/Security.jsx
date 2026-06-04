import Section from '../components/Section.jsx'
import Reveal from '../components/Reveal.jsx'
import { Link } from 'react-router-dom'
import { IconShield, IconLock, IconRoute, IconCheck } from '../components/icons.jsx'

const points = [
  {
    icon: <IconLock width={20} height={20} />,
    title: 'Minimización de datos',
    text: 'Solo se tratan los datos necesarios para prestar el servicio solicitado.',
  },
  {
    icon: <IconShield width={20} height={20} />,
    title: 'El negocio mantiene el control',
    text: 'Tú sigues siendo el responsable de la relación con tus clientes y de su información.',
  },
  {
    icon: <IconRoute width={20} height={20} />,
    title: 'Diseño orientado al cumplimiento',
    text: 'Pensado desde el inicio en trazabilidad, control y minimización de datos.',
  },
]

export default function Security() {
  return (
    <Section
      id="seguridad"
      eyebrow="Seguridad y privacidad"
      title="Diseñado con privacidad y control desde el inicio"
      subtitle="La protección de los datos de tus clientes es parte del diseño, no un añadido posterior."
    >
      <div className="mt-14 grid gap-5 sm:grid-cols-3">
        {points.map((p, i) => (
          <Reveal key={p.title} delay={i * 80}>
            <div className="card-ring h-full p-6">
              <div className="mb-4 inline-flex h-11 w-11 items-center justify-center rounded-2xl bg-brand-gradient-soft text-brand-600 ring-1 ring-brand-100">
                {p.icon}
              </div>
              <h3 className="text-base font-semibold text-ink">{p.title}</h3>
              <p className="mt-2 text-[15px] leading-relaxed text-ink-muted">{p.text}</p>
            </div>
          </Reveal>
        ))}
      </div>

      <Reveal delay={240}>
        <div className="mx-auto mt-8 flex max-w-3xl flex-col items-start gap-3 rounded-3xl border border-ink/5 bg-[#fafafe] p-6 sm:flex-row sm:items-center sm:justify-between">
          <p className="flex items-center gap-2.5 text-sm text-ink-soft">
            <span className="text-brand-600">
              <IconCheck width={18} height={18} />
            </span>
            Los usuarios pueden solicitar la eliminación de sus datos en cualquier momento.
          </p>
          <Link
            to="/data-deletion"
            className="shrink-0 text-sm font-semibold text-brand-700 hover:text-brand-800"
          >
            Cómo solicitar la eliminación →
          </Link>
        </div>
      </Reveal>
    </Section>
  )
}
