import Section from '../components/Section.jsx'
import Reveal from '../components/Reveal.jsx'
import FeatureCard from '../components/FeatureCard.jsx'
import {
  IconClock,
  IconChart,
  IconBolt,
  IconUsers,
  IconRefresh,
  IconLayers,
} from '../components/icons.jsx'

const benefits = [
  {
    icon: <IconClock width={22} height={22} />,
    title: 'Atención 24/7',
    description: 'Tus clientes reciben respuesta al instante, incluso fuera del horario de apertura.',
  },
  {
    icon: <IconChart width={22} height={22} />,
    title: 'Más citas cerradas',
    description: 'Respuestas inmediatas que evitan que el cliente se enfríe o se vaya a la competencia.',
  },
  {
    icon: <IconBolt width={22} height={22} />,
    title: 'Menos carga administrativa',
    description: 'El equipo se libera de tareas repetitivas y se centra en lo que de verdad importa.',
  },
  {
    icon: <IconUsers width={22} height={22} />,
    title: 'Mejor experiencia del cliente',
    description: 'Trato ágil, cercano y sin esperas, en el canal que ya usan a diario.',
  },
  {
    icon: <IconRefresh width={22} height={22} />,
    title: 'Respuestas consistentes',
    description: 'La misma información, siempre correcta y alineada con las reglas de tu negocio.',
  },
  {
    icon: <IconLayers width={22} height={22} />,
    title: 'Escalable',
    description: 'Funciona igual de bien con una sede o con varios profesionales y ubicaciones.',
  },
]

export default function Benefits() {
  return (
    <Section
      id="beneficios"
      className="bg-[#fafafe]"
      eyebrow="Beneficios"
      title="Lo que gana tu negocio con Kora"
      subtitle="No es solo automatizar respuestas: es recuperar tiempo, cerrar más citas y dar una mejor atención."
    >
      <div className="mt-14 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        {benefits.map((b, i) => (
          <Reveal key={b.title} delay={i * 60}>
            <FeatureCard {...b} />
          </Reveal>
        ))}
      </div>
    </Section>
  )
}
