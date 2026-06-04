import LegalPageLayout from '../components/LegalPageLayout.jsx'
import { site } from '../config/site.js'

export default function TermsAndConditions() {
  return (
    <LegalPageLayout
      title="Términos y Condiciones"
      seoDescription="Términos y Condiciones de uso del servicio de Kora Software."
    >
      <p className="lead">
        Estos Términos y Condiciones regulan el acceso y uso del servicio de{' '}
        {site.brand} ({site.group}). Al utilizar el servicio, aceptas estos
        términos. Si no estás de acuerdo, te pedimos que no lo utilices.
      </p>

      <h2>1. Descripción del servicio</h2>
      <p>
        {site.brand} ofrece agentes de inteligencia artificial para la
        automatización de la atención al cliente, la gestión de citas y las
        respuestas a través de canales digitales como WhatsApp. El servicio puede
        prestarse directamente a usuarios finales o por cuenta de un negocio
        cliente que lo contrata para gestionar sus propias comunicaciones.
      </p>

      <h2>2. Uso permitido</h2>
      <p>Al utilizar el servicio te comprometes a:</p>
      <ul>
        <li>Proporcionar información veraz y actualizada.</li>
        <li>Utilizar el servicio conforme a la ley y a estos términos.</li>
        <li>No emplearlo para fines fraudulentos, ilícitos o abusivos.</li>
        <li>
          No intentar interferir, dañar o acceder de forma no autorizada a los
          sistemas que soportan el servicio.
        </li>
      </ul>

      <h2>3. Limitaciones del servicio</h2>
      <p>
        El servicio se apoya en tecnologías de inteligencia artificial. Por su
        naturaleza, <strong>la IA puede cometer errores</strong>, generar respuestas
        inexactas o incompletas, y algunas solicitudes pueden requerir revisión o
        intervención humana. No debes basar decisiones importantes únicamente en las
        respuestas automatizadas sin la confirmación correspondiente.
      </p>

      <h2>4. No sustituye asesoramiento profesional</h2>
      <p>
        {site.brand} <strong>no presta ni sustituye</strong> asesoramiento médico,
        legal, financiero ni profesional de ningún tipo. Las respuestas del agente
        tienen carácter informativo y operativo (por ejemplo, gestión de citas) y no
        deben interpretarse como un diagnóstico, recomendación profesional o consejo
        cualificado.
      </p>

      <h2>5. Responsabilidad del negocio cliente</h2>
      <p>
        Cuando el servicio se utiliza por cuenta de un negocio cliente, dicho negocio
        es responsable de la exactitud, legalidad y actualización de la información
        que configura en el sistema (horarios, precios, servicios, reglas, mensajes,
        etc.), así como del cumplimiento de las obligaciones que le correspondan
        frente a sus propios clientes.
      </p>

      <h2>6. Disponibilidad del servicio</h2>
      <p>
        Trabajamos para ofrecer un servicio estable y disponible, pero no podemos
        garantizar que funcione de forma ininterrumpida o libre de errores. El
        servicio puede verse afectado por mantenimientos, actualizaciones o por
        servicios de terceros (incluida la disponibilidad de plataformas de
        mensajería) ajenos a nuestro control.
      </p>

      <h2>7. Propiedad intelectual</h2>
      <p>
        El servicio, su software, marca, diseño y contenidos son titularidad de{' '}
        {site.brand} / {site.group} o de sus licenciantes, y están protegidos por la
        normativa aplicable. No se concede ningún derecho sobre los mismos más allá
        del uso necesario para utilizar el servicio conforme a estos términos.
      </p>

      <h2>8. Limitación de responsabilidad</h2>
      <p>
        En la medida permitida por la ley, {site.brand} no será responsable de daños
        indirectos, lucro cesante o pérdidas derivadas del uso o la imposibilidad de
        uso del servicio, ni de errores en respuestas automatizadas que el usuario o
        el negocio cliente no hayan verificado cuando ello resultaba razonable.
      </p>

      <h2>9. Suspensión o terminación</h2>
      <p>
        Podemos suspender o finalizar el acceso al servicio en caso de uso indebido,
        incumplimiento de estos términos o cuando sea necesario por razones técnicas,
        legales o de seguridad.
      </p>

      <h2>10. Modificaciones</h2>
      <p>
        Podemos actualizar estos Términos y Condiciones. Publicaremos la versión
        vigente en esta página, indicando su fecha de entrada en vigor.
      </p>

      <h2>11. Legislación aplicable</h2>
      <p>
        Salvo que la normativa imperativa disponga otra cosa, estos términos se rigen
        por la legislación de {site.country}.
      </p>

      <h2>12. Contacto</h2>
      <p>
        Para cualquier cuestión relativa a estos términos, escríbenos a{' '}
        <a href={`mailto:${site.email}`}>{site.email}</a>.
      </p>
    </LegalPageLayout>
  )
}
