import Reveal from '../components/Reveal.jsx'
import ContactForm from '../components/ContactForm.jsx'
import { site } from '../config/site.js'
import { IconChat, IconClock, IconShield } from '../components/icons.jsx'

const highlights = [
  {
    icon: <IconChat width={20} height={20} />,
    title: 'Demo personalizada',
    text: 'Te mostramos cómo Kora respondería a los casos reales de tu negocio.',
  },
  {
    icon: <IconClock width={20} height={20} />,
    title: 'Sin compromiso',
    text: 'Una conversación para ver si encaja con lo que necesitas. Sin presión.',
  },
  {
    icon: <IconShield width={20} height={20} />,
    title: 'Privacidad por diseño',
    text: 'Tratamos solo los datos necesarios y tú mantienes el control.',
  },
]

export default function ContactSection() {
  return (
    <section id="contacto" className="py-20 sm:py-28">
      <div className="container-kora grid gap-12 lg:grid-cols-2 lg:gap-16">
        <Reveal>
          <span className="eyebrow">Contacto</span>
          <h2 className="mt-5 text-3xl font-bold tracking-tight text-ink sm:text-4xl md:text-[2.6rem] md:leading-[1.1]">
            Solicita una demo de Kora
          </h2>
          <p className="mt-5 text-lg leading-relaxed text-ink-muted">
            Cuéntanos sobre tu negocio y te enseñamos cómo automatizar tus
            conversaciones, citas y tareas repetitivas con agentes de IA.
          </p>

          <ul className="mt-8 space-y-5">
            {highlights.map((h) => (
              <li key={h.title} className="flex gap-4">
                <span className="grid h-11 w-11 shrink-0 place-items-center rounded-2xl bg-brand-gradient-soft text-brand-600 ring-1 ring-brand-100">
                  {h.icon}
                </span>
                <div>
                  <h3 className="text-base font-semibold text-ink">{h.title}</h3>
                  <p className="mt-1 text-[15px] leading-relaxed text-ink-muted">{h.text}</p>
                </div>
              </li>
            ))}
          </ul>

          <p className="mt-8 text-sm text-ink-muted">
            Email directo:{' '}
            <a
              href={`mailto:${site.email}`}
              className="font-semibold text-brand-700 hover:text-brand-800"
            >
              {site.email}
            </a>
          </p>
        </Reveal>

        <Reveal delay={120}>
          <ContactForm />
        </Reveal>
      </div>
    </section>
  )
}
