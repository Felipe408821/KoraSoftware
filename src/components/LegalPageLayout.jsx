import { Link } from 'react-router-dom'
import SEO from './SEO.jsx'
import { site } from '../config/site.js'
import { IconArrowRight, IconAlert } from './icons.jsx'

// Layout para páginas legales: cabecera, fecha de vigencia, aviso de plantilla,
// contenido (prose) y navegación entre documentos.
const legalNav = [
  { label: 'Política de Privacidad', to: '/privacy-policy' },
  { label: 'Términos y Condiciones', to: '/terms-and-conditions' },
  { label: 'Eliminación de Datos', to: '/data-deletion' },
  { label: 'Política de Cookies', to: '/cookies-policy' },
  { label: 'Contacto', to: '/contact' },
]

export default function LegalPageLayout({
  title,
  seoTitle,
  seoDescription,
  effectiveDate = site.legalEffectiveDate,
  children,
}) {
  return (
    <div className="relative">
      <SEO title={seoTitle || title} description={seoDescription} />

      {/* Fondo decorativo superior */}
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
            {title}
          </h1>
          {effectiveDate && (
            <p className="mt-3 text-sm text-ink-muted">
              Fecha de entrada en vigor: <strong>{effectiveDate}</strong>
            </p>
          )}

          {/* Contenido del documento */}
          <article className="legal-prose mt-10">{children}</article>

          {/* Navegación entre documentos legales */}
          <div className="mt-16 border-t border-ink/5 pt-8">
            <h2 className="text-xs font-semibold uppercase tracking-wider text-ink-muted">
              Otros documentos
            </h2>
            <ul className="mt-4 flex flex-wrap gap-2">
              {legalNav
                .filter((l) => l.label !== title)
                .map((l) => (
                  <li key={l.to}>
                    <Link
                      to={l.to}
                      className="inline-flex rounded-full border border-ink/10 bg-white px-4 py-2 text-sm font-medium text-ink-soft transition-colors hover:border-brand-300 hover:text-brand-700"
                    >
                      {l.label}
                    </Link>
                  </li>
                ))}
            </ul>
          </div>
        </div>
      </div>
    </div>
  )
}
