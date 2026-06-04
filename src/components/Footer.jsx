import { Link } from 'react-router-dom'
import Logo from './Logo.jsx'
import { site } from '../config/site.js'

const legalLinks = [
  { label: 'Privacy Policy', to: '/privacy-policy' },
  { label: 'Terms and Conditions', to: '/terms-and-conditions' },
  { label: 'Data Deletion', to: '/data-deletion' },
  { label: 'Cookies Policy', to: '/cookies-policy' },
  { label: 'Contact', to: '/contact' },
]

export default function Footer() {
  return (
    <footer className="border-t border-ink/5 bg-[#fafafe]">
      <div className="container-kora py-14">
        <div className="flex flex-col gap-10 md:flex-row md:items-start md:justify-between">
          <div className="max-w-sm">
            <Logo />
            <p className="mt-4 text-sm leading-relaxed text-ink-muted">
              {site.tagline} Parte de {site.group}.
            </p>
            <p className="mt-3 text-sm text-ink-muted">
              <a
                href={`mailto:${site.email}`}
                className="font-medium text-brand-700 hover:text-brand-800"
              >
                {site.email}
              </a>
            </p>
          </div>

          <div className="grid grid-cols-2 gap-8 sm:grid-cols-2">
            <div>
              <h4 className="text-xs font-semibold uppercase tracking-wider text-ink">
                Legal
              </h4>
              <ul className="mt-4 space-y-3">
                {legalLinks.map((link) => (
                  <li key={link.to}>
                    <Link
                      to={link.to}
                      className="text-sm text-ink-muted transition-colors hover:text-brand-700"
                    >
                      {link.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
            <div>
              <h4 className="text-xs font-semibold uppercase tracking-wider text-ink">
                Producto
              </h4>
              <ul className="mt-4 space-y-3 text-sm text-ink-muted">
                <li>KoraBusinessAgents</li>
                <li>Atención por WhatsApp</li>
                <li>Gestión de citas</li>
                <li>Automatización de tareas</li>
              </ul>
            </div>
          </div>
        </div>

        <div className="mt-12 flex flex-col gap-4 border-t border-ink/5 pt-6 text-sm text-ink-muted sm:flex-row sm:items-center sm:justify-between">
          <p>© {site.copyrightYear} {site.brand}. All rights reserved.</p>
          <p className="text-xs">
            Kora Software is not affiliated with WhatsApp or Meta. «WhatsApp» se
            menciona únicamente de forma descriptiva.
          </p>
        </div>
      </div>
    </footer>
  )
}
