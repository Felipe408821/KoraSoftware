import Section from '../components/Section.jsx'
import Reveal from '../components/Reveal.jsx'
import {
  IconClock,
  IconUsers,
  IconCalendar,
  IconRefresh,
  IconChat,
  IconChart,
} from '../components/icons.jsx'

const problems = [
  {
    icon: <IconClock width={20} height={20} />,
    title: 'Mensajes fuera de horario',
    text: 'Los clientes escriben de noche o en fin de semana, cuando nadie puede responder.',
  },
  {
    icon: <IconUsers width={20} height={20} />,
    title: 'Recepción saturada',
    text: 'El teléfono y los chats se acumulan mientras el equipo atiende en consulta.',
  },
  {
    icon: <IconCalendar width={20} height={20} />,
    title: 'Citas que se pierden',
    text: 'Sin respuesta rápida, el cliente se va a otro sitio o no llega a reservar.',
  },
  {
    icon: <IconRefresh width={20} height={20} />,
    title: 'Preguntas repetidas',
    text: 'Horarios, precios, ubicación, servicios… las mismas dudas una y otra vez.',
  },
  {
    icon: <IconChat width={20} height={20} />,
    title: 'Falta de seguimiento',
    text: 'Conversaciones sin cerrar y recordatorios que nadie llega a enviar.',
  },
  {
    icon: <IconChart width={20} height={20} />,
    title: 'Tiempo administrativo',
    text: 'Horas dedicadas a tareas repetitivas que aportan poco valor al negocio.',
  },
]

export default function Problem() {
  return (
    <Section
      id="problema"
      eyebrow="El problema"
      title="Tus clientes escriben. Tu equipo no siempre puede responder."
      subtitle="Cada mensaje sin contestar es una oportunidad que se enfría. Estos son los puntos de fricción más habituales en negocios de servicios."
    >
      <div className="mt-14 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        {problems.map((p, i) => (
          <Reveal key={p.title} delay={i * 60}>
            <div className="card-ring h-full p-6">
              <div className="mb-4 inline-flex h-11 w-11 items-center justify-center rounded-2xl bg-rose-50 text-rose-500 ring-1 ring-rose-100">
                {p.icon}
              </div>
              <h3 className="text-base font-semibold text-ink">{p.title}</h3>
              <p className="mt-2 text-[15px] leading-relaxed text-ink-muted">{p.text}</p>
            </div>
          </Reveal>
        ))}
      </div>
    </Section>
  )
}
