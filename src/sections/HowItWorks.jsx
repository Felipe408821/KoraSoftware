import Section from '../components/Section.jsx'
import Reveal from '../components/Reveal.jsx'
import { IconChat, IconSparkle, IconCalendar, IconCheck } from '../components/icons.jsx'

const steps = [
  {
    icon: <IconChat width={22} height={22} />,
    title: 'El cliente escribe',
    text: 'Un paciente o cliente envía un mensaje por WhatsApp, a cualquier hora.',
  },
  {
    icon: <IconSparkle width={22} height={22} />,
    title: 'El agente entiende',
    text: 'Kora interpreta la intención del mensaje: una cita, una duda, una urgencia…',
  },
  {
    icon: <IconCalendar width={22} height={22} />,
    title: 'Consulta tus reglas',
    text: 'Comprueba disponibilidad, horarios, servicios y las reglas de tu negocio.',
  },
  {
    icon: <IconCheck width={22} height={22} />,
    title: 'Respuesta y gestión',
    text: 'El cliente recibe una respuesta clara y la cita queda gestionada y confirmada.',
  },
]

export default function HowItWorks() {
  return (
    <Section
      id="como-funciona"
      eyebrow="Cómo funciona"
      title="De un mensaje a una cita gestionada en cuatro pasos"
      subtitle="Sin formularios complicados ni esperas. Una conversación natural que termina en una acción concreta."
    >
      <div className="mt-16 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        {steps.map((s, i) => (
          <Reveal key={s.title} delay={i * 90}>
            <div className="relative h-full">
              <div className="card-ring h-full p-6">
                <div className="flex items-center justify-between">
                  <span className="inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-brand-gradient text-white shadow-glow">
                    {s.icon}
                  </span>
                  <span className="text-4xl font-bold text-brand-100">
                    {String(i + 1).padStart(2, '0')}
                  </span>
                </div>
                <h3 className="mt-5 text-base font-semibold text-ink">{s.title}</h3>
                <p className="mt-2 text-[15px] leading-relaxed text-ink-muted">{s.text}</p>
              </div>
            </div>
          </Reveal>
        ))}
      </div>
    </Section>
  )
}
