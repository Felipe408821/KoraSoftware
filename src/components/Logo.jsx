import { Link } from 'react-router-dom'

// Logo textual de Kora Software con marca gráfica simple (anillo + punto).
export default function Logo({ className = '', withText = true }) {
  return (
    <Link
      to="/"
      aria-label="Kora Software — Inicio"
      className={`group inline-flex items-center gap-2.5 ${className}`}
    >
      <span className="relative grid h-9 w-9 place-items-center rounded-xl bg-brand-gradient shadow-glow transition-transform duration-300 group-hover:scale-105">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">
          <circle cx="12" cy="12" r="7.5" stroke="white" strokeWidth="2" opacity="0.95" />
          <circle cx="12" cy="12" r="2.6" fill="white" />
        </svg>
      </span>
      {withText && (
        <span className="text-[1.05rem] font-bold tracking-tight text-ink">
          Kora <span className="font-semibold text-ink-soft">Software</span>
        </span>
      )}
    </Link>
  )
}
