import { Link } from 'react-router-dom'
import SEO from '../components/SEO.jsx'
import ContactForm from '../components/ContactForm.jsx'
import { site } from '../config/site.js'
import { IconArrowRight } from '../components/icons.jsx'

export default function Contact() {
  return (
    <div className="relative">
      <SEO
        title="Contacto"
        description="Contacta con Kora Software para solicitar una demo de agentes de IA para la atención por WhatsApp."
      />

      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-x-0 top-0 -z-10 h-72 bg-gradient-to-b from-brand-50/70 to-transparent"
      />

      <div className="container-kora py-16 sm:py-20">
        <div className="mx-auto max-w-3xl">
          <Link
            to="/"
            className="inline-flex items-center gap-1.5 text-sm font-medium text-brand-700 hover:text-brand-800"
          >
            <span className="rotate-180">
              <IconArrowRight width={16} height={16} />
            </span>
            Volver al inicio
          </Link>

          <h1 className="mt-6 text-3xl font-bold tracking-tight text-ink sm:text-4xl">
            Hablemos
          </h1>
          <p className="mt-4 max-w-2xl text-lg leading-relaxed text-ink-muted">
            ¿Quieres ver Kora en acción? Déjanos tus datos y te preparamos una
            demo adaptada a tu negocio. También puedes escribirnos directamente a{' '}
            <a
              href={`mailto:${site.email}`}
              className="font-semibold text-brand-700 hover:text-brand-800"
            >
              {site.email}
            </a>
            .
          </p>

          <div className="mt-10">
            <ContactForm />
          </div>
        </div>
      </div>
    </div>
  )
}
