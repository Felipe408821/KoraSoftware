import { useEffect, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import Logo from './Logo.jsx'
import Button from './Button.jsx'
import { demoMailto } from '../config/site.js'

const navLinks = [
  { label: 'Solución', anchor: 'solucion' },
  { label: 'Cómo funciona', anchor: 'como-funciona' },
  { label: 'Beneficios', anchor: 'beneficios' },
  { label: 'Casos de uso', anchor: 'casos-de-uso' },
  { label: 'Contacto', anchor: 'contacto' },
]

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false)
  const [open, setOpen] = useState(false)
  const location = useLocation()
  const navigate = useNavigate()

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8)
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  // Bloquea el scroll del body cuando el menú móvil está abierto
  useEffect(() => {
    document.body.style.overflow = open ? 'hidden' : ''
    return () => {
      document.body.style.overflow = ''
    }
  }, [open])

  // Navega a una sección de la home (desde cualquier ruta)
  const goToSection = (anchor) => {
    setOpen(false)
    if (location.pathname === '/') {
      const el = document.getElementById(anchor)
      if (el) el.scrollIntoView({ behavior: 'smooth' })
    } else {
      navigate(`/#${anchor}`)
    }
  }

  return (
    <header
      className={`fixed inset-x-0 top-0 z-50 transition-all duration-300 ${
        scrolled
          ? 'border-b border-ink/5 bg-white/80 backdrop-blur-xl'
          : 'border-b border-transparent bg-transparent'
      }`}
    >
      <nav className="container-kora flex h-16 items-center justify-between sm:h-18">
        <Logo />

        {/* Navegación desktop */}
        <div className="hidden items-center gap-1 lg:flex">
          {navLinks.map((link) => (
            <button
              key={link.anchor}
              onClick={() => goToSection(link.anchor)}
              className="rounded-full px-3.5 py-2 text-sm font-medium text-ink-soft transition-colors hover:bg-brand-50 hover:text-brand-700"
            >
              {link.label}
            </button>
          ))}
        </div>

        <div className="hidden items-center gap-3 lg:flex">
          <Button href={demoMailto} size="md">
            Solicitar demo
          </Button>
        </div>

        {/* Botón menú móvil */}
        <button
          onClick={() => setOpen((v) => !v)}
          aria-label={open ? 'Cerrar menú' : 'Abrir menú'}
          aria-expanded={open}
          className="grid h-10 w-10 place-items-center rounded-xl border border-ink/10 text-ink lg:hidden"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
            {open ? <path d="M6 6l12 12M18 6L6 18" /> : <path d="M4 7h16M4 12h16M4 17h16" />}
          </svg>
        </button>
      </nav>

      {/* Panel móvil */}
      {open && (
        <div className="lg:hidden">
          <div className="container-kora animate-fade-up border-t border-ink/5 bg-white pb-6 pt-2">
            <div className="flex flex-col">
              {navLinks.map((link) => (
                <button
                  key={link.anchor}
                  onClick={() => goToSection(link.anchor)}
                  className="rounded-xl px-3 py-3 text-left text-base font-medium text-ink-soft transition-colors hover:bg-brand-50 hover:text-brand-700"
                >
                  {link.label}
                </button>
              ))}
            </div>
            <Button href={demoMailto} size="lg" className="mt-4 w-full">
              Solicitar demo
            </Button>
          </div>
        </div>
      )}
    </header>
  )
}
