import LegalPageLayout from '../components/LegalPageLayout.jsx'
import { site } from '../config/site.js'

export default function DataDeletion() {
  return (
    <LegalPageLayout
      title="User Data Deletion Instructions"
      seoTitle="Instrucciones de Eliminación de Datos"
      seoDescription="Cómo solicitar la eliminación de tus datos personales tratados por Kora Software. How to request deletion of your personal data."
    >
      {/* ----------------------------- ESPAÑOL ----------------------------- */}
      <h2>Instrucciones de Eliminación de Datos (Español)</h2>
      <p>
        Los usuarios pueden solicitar la eliminación de sus datos personales
        tratados por {site.brand} ({site.group}).
      </p>

      <h3>Cómo solicitar la eliminación</h3>
      <ol>
        <li>
          Envía un email a <a href={`mailto:${site.email}`}>{site.email}</a>.
        </li>
        <li>
          Indica como asunto: <strong>«Data Deletion Request»</strong>.
        </li>
        <li>
          Incluye tu nombre, el número de teléfono asociado a tu interacción y una
          breve descripción de tu solicitud.
        </li>
      </ol>
      <p>
        Kora verificará la solicitud cuando sea necesario para confirmar tu
        identidad. Una vez verificada, eliminaremos o anonimizaremos tus datos,
        salvo aquellos que debamos conservar por obligación legal, por motivos de
        seguridad o para la resolución de disputas. Responderemos a tu solicitud en
        un plazo razonable.
      </p>

      <h3>Usuarios de Meta / WhatsApp</h3>
      <p>
        Si interactuaste con {site.brand} a través de WhatsApp u otro servicio de
        Meta, también puedes gestionar tu información desde la configuración de tu
        cuenta de WhatsApp o de Meta, sujeto a las políticas propias de Meta.{' '}
        {site.brand} no está afiliada a WhatsApp ni a Meta.
      </p>

      <hr />

      {/* ----------------------------- ENGLISH ----------------------------- */}
      <h2>User Data Deletion Instructions (English)</h2>
      <p>
        Users may request the deletion of their personal data processed by{' '}
        {site.brand} ({site.group}).
      </p>

      <h3>How to request deletion</h3>
      <ol>
        <li>
          Send an email to <a href={`mailto:${site.email}`}>{site.email}</a>.
        </li>
        <li>
          Use the subject line: <strong>“Data Deletion Request”</strong>.
        </li>
        <li>
          Include your name, the phone number associated with your interaction, and
          a short description of your request.
        </li>
      </ol>
      <p>
        Kora will verify the request where necessary to confirm your identity. Once
        verified, we will delete or anonymize your data, except for data we are
        required to retain due to legal obligations, security reasons, or the
        resolution of disputes. We will respond to your request within a reasonable
        timeframe.
      </p>

      <h3>Meta / WhatsApp users</h3>
      <p>
        If you interacted with {site.brand} through WhatsApp or another Meta service,
        you may also manage your information through your WhatsApp or Meta account
        settings, subject to Meta’s own policies. {site.brand} is not affiliated with
        WhatsApp or Meta.
      </p>

      <hr />

      <p>
        <strong>Contact / Contacto:</strong>{' '}
        <a href={`mailto:${site.email}`}>{site.email}</a>
      </p>
    </LegalPageLayout>
  )
}
