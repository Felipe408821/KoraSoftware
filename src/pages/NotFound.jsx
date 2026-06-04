import SEO from '../components/SEO.jsx'
import Button from '../components/Button.jsx'
import { IconArrowRight } from '../components/icons.jsx'

export default function NotFound() {
  return (
    <div className="container-kora flex min-h-[60vh] flex-col items-center justify-center py-20 text-center">
      <SEO title="Página no encontrada" />
      <span className="text-7xl font-bold text-gradient">404</span>
      <h1 className="mt-4 text-2xl font-bold text-ink">Esta página no existe</h1>
      <p className="mt-3 max-w-md text-ink-muted">
        Es posible que el enlace haya cambiado o que la página se haya movido.
      </p>
      <Button to="/" size="lg" className="mt-8">
        Volver al inicio
        <IconArrowRight width={18} height={18} />
      </Button>
    </div>
  )
}
