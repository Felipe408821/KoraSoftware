import LegalPageLayout from '../components/LegalPageLayout.jsx'
import { site } from '../config/site.js'

export default function CookiesPolicy() {
  return (
    <LegalPageLayout
      title="Política de Cookies"
      seoDescription="Política de Cookies de Kora Software. Actualmente el sitio no utiliza cookies de análisis ni de publicidad."
    >
      <p className="lead">
        Esta Política de Cookies explica el uso de cookies y tecnologías similares en
        el sitio web de {site.brand}.
      </p>

      <h2>1. Situación actual</h2>
      <p>
        Actualmente, este sitio web <strong>no utiliza cookies de análisis ni de
        publicidad</strong>, ni tecnologías de seguimiento de terceros. No
        elaboramos perfiles de navegación ni compartimos tu actividad con terceros
        con fines publicitarios.
      </p>

      <h2>2. Cookies técnicas necesarias</h2>
      <p>
        En el futuro, el sitio podría utilizar cookies técnicas estrictamente
        necesarias para su funcionamiento (por ejemplo, para recordar preferencias
        básicas o garantizar la seguridad), si se añaden funcionalidades que las
        requieran. Este tipo de cookies no requieren consentimiento previo conforme
        a la normativa aplicable.
      </p>

      <h2>3. Cambios futuros</h2>
      <p>
        Si en el futuro incorporamos herramientas de analítica, píxeles de
        seguimiento o servicios de terceros, actualizaremos esta política y, cuando
        sea legalmente exigible, solicitaremos tu consentimiento mediante un sistema
        de gestión de cookies antes de activarlas.
      </p>

      <h2>4. Cómo gestionar las cookies</h2>
      <p>
        Puedes configurar tu navegador para bloquear o eliminar cookies en cualquier
        momento. Ten en cuenta que, si en el futuro se utilizan cookies necesarias,
        bloquearlas podría afectar al funcionamiento de algunas partes del sitio.
      </p>

      <h2>5. Contacto</h2>
      <p>
        Para cualquier duda sobre esta Política de Cookies, escríbenos a{' '}
        <a href={`mailto:${site.email}`}>{site.email}</a>.
      </p>
    </LegalPageLayout>
  )
}
