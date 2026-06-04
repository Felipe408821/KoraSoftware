import LegalPageLayout from '../components/LegalPageLayout.jsx'
import { site } from '../config/site.js'

export default function PrivacyPolicy() {
  return (
    <LegalPageLayout
      title="Política de Privacidad"
      seoDescription="Política de Privacidad de Kora Software: qué datos tratamos, con qué finalidad, base legal y cómo ejercer tus derechos."
    >
      <p className="lead">
        Esta Política de Privacidad explica cómo {site.brand} ({site.group}) trata
        los datos personales en el marco de su servicio de agentes de inteligencia
        artificial para la automatización de la atención al cliente, la gestión de
        citas y las respuestas a través de canales digitales como WhatsApp.
      </p>

      <h2>1. Quiénes somos</h2>
      <p>
        {site.brand}, marca perteneciente a {site.group} (en adelante, «Kora»,
        «nosotros»), con base inicial en {site.country}, es responsable del
        tratamiento de los datos personales descritos en esta política en relación
        con la prestación de su servicio.
      </p>
      <p>
        Para cualquier cuestión relativa a privacidad puedes escribirnos a{' '}
        <a href={`mailto:${site.email}`}>{site.email}</a>.
      </p>
      <p>
        En muchos casos, Kora presta sus servicios <strong>por cuenta de un
        negocio cliente</strong> (por ejemplo, una clínica). En esos supuestos, el
        negocio cliente actúa como responsable del tratamiento de los datos de sus
        propios clientes y Kora actúa como encargado del tratamiento, tratando los
        datos siguiendo sus instrucciones y un contrato de encargo.
      </p>

      <h2>2. Qué datos podemos tratar</h2>
      <p>Dependiendo de tu interacción, podemos tratar las siguientes categorías de datos:</p>
      <ul>
        <li>Nombre.</li>
        <li>Número de teléfono.</li>
        <li>Mensajes y contenido enviado por el usuario en la conversación.</li>
        <li>Datos relativos a la cita (fecha, hora, profesional, sede).</li>
        <li>Servicio solicitado.</li>
        <li>Fecha y hora preferidas.</li>
        <li>Información necesaria para gestionar tu solicitud.</li>
        <li>
          Metadatos técnicos mínimos (por ejemplo, marcas de tiempo o
          identificadores necesarios para el funcionamiento del servicio).
        </li>
      </ul>
      <p>
        Te pedimos que no compartas datos sensibles (por ejemplo, información de
        salud detallada) más allá de lo estrictamente necesario para gestionar tu
        solicitud.
      </p>

      <h2>3. Finalidades del tratamiento</h2>
      <ul>
        <li>Responder a tus solicitudes y consultas.</li>
        <li>Gestionar citas (creación, modificación, cancelación y recordatorios).</li>
        <li>Prestar soporte y atención.</li>
        <li>Mejorar y mantener la calidad del servicio.</li>
        <li>Cumplir con las obligaciones legales aplicables.</li>
      </ul>

      <h2>4. Base legal del tratamiento</h2>
      <ul>
        <li>
          <strong>Consentimiento</strong>, cuando inicias una conversación o nos
          facilitas tus datos voluntariamente.
        </li>
        <li>
          <strong>Ejecución de un servicio solicitado</strong> o de medidas
          precontractuales adoptadas a tu petición.
        </li>
        <li>
          <strong>Interés legítimo</strong>, para garantizar el funcionamiento,
          la seguridad y la mejora del servicio, ponderado con tus derechos.
        </li>
        <li>
          <strong>Cumplimiento de obligaciones legales</strong>, cuando
          corresponda.
        </li>
      </ul>

      <h2>5. Uso de WhatsApp / Meta</h2>
      <p>
        La comunicación con Kora puede producirse a través de la WhatsApp Business
        Platform. El uso de WhatsApp está sujeto también a las{' '}
        <a href="https://www.whatsapp.com/legal/" target="_blank" rel="noreferrer noopener">
          políticas y condiciones de WhatsApp/Meta
        </a>
        , sobre las que Kora no tiene control. {site.brand} no está afiliada a
        WhatsApp ni a Meta; «WhatsApp» se menciona únicamente de forma descriptiva.
      </p>

      <h2>6. Encargados y proveedores</h2>
      <p>
        Para prestar el servicio podemos apoyarnos en proveedores que tratan datos
        por cuenta de Kora bajo las garantías contractuales adecuadas, tales como:
      </p>
      <ul>
        <li>Proveedores de alojamiento (hosting) e infraestructura.</li>
        <li>Servicios de mensajería y comunicaciones.</li>
        <li>Servicios de calendario y agenda.</li>
        <li>Herramientas de automatización y modelos de IA.</li>
      </ul>

      <h2>7. Conservación de los datos</h2>
      <p>
        Conservamos los datos personales únicamente durante el tiempo necesario
        para prestar el servicio solicitado y, posteriormente, durante los plazos
        que resulten exigibles para cumplir obligaciones legales o atender posibles
        responsabilidades. Cuando dejan de ser necesarios, se eliminan o anonimizan.
      </p>

      <h2>8. Tus derechos</h2>
      <p>Puedes ejercer en cualquier momento los siguientes derechos:</p>
      <ul>
        <li>Acceso.</li>
        <li>Rectificación.</li>
        <li>Eliminación (supresión).</li>
        <li>Oposición.</li>
        <li>Limitación del tratamiento.</li>
        <li>Portabilidad, cuando resulte aplicable.</li>
      </ul>
      <p>
        Para ejercerlos, escríbenos a{' '}
        <a href={`mailto:${site.email}`}>{site.email}</a>. También tienes derecho a
        presentar una reclamación ante la autoridad de control competente (en
        España, la Agencia Española de Protección de Datos, www.aepd.es).
      </p>

      <h2>9. Cómo solicitar la eliminación de tus datos</h2>
      <p>Para solicitar la eliminación de tus datos personales:</p>
      <ol>
        <li>
          Envía un email a <a href={`mailto:${site.email}`}>{site.email}</a>.
        </li>
        <li>Indica el número de teléfono asociado a tu interacción.</li>
        <li>Describe brevemente tu solicitud.</li>
      </ol>
      <p>
        Consulta también nuestras{' '}
        <a href="#/data-deletion">Instrucciones de Eliminación de Datos</a> para más
        detalle.
      </p>

      <h2>10. Seguridad</h2>
      <p>
        Aplicamos medidas técnicas y organizativas razonables para proteger los
        datos personales frente a accesos no autorizados, pérdida o alteración.
        Ningún sistema es completamente infalible, por lo que no podemos garantizar
        una seguridad absoluta, pero trabajamos para reducir los riesgos de forma
        proporcional a la naturaleza de los datos.
      </p>

      <h2>11. Transferencias internacionales</h2>
      <p>
        Algunos de nuestros proveedores pueden tratar datos fuera del Espacio
        Económico Europeo. Cuando esto ocurra, adoptaremos las garantías adecuadas
        previstas por la normativa aplicable (por ejemplo, cláusulas contractuales
        tipo) para proteger tus datos.
      </p>

      <h2>12. Cambios en esta política</h2>
      <p>
        Podemos actualizar esta Política de Privacidad para reflejar cambios en el
        servicio o en la normativa. Publicaremos la versión vigente en esta página
        e indicaremos su fecha de entrada en vigor.
      </p>

      <h2>13. Contacto</h2>
      <p>
        Para cualquier duda sobre esta política o sobre el tratamiento de tus datos,
        contacta con nosotros en{' '}
        <a href={`mailto:${site.email}`}>{site.email}</a>.
      </p>
    </LegalPageLayout>
  )
}
