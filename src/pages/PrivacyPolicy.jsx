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

      <h1>Política de Privacidad y Tratamiento de Datos Personales</h1>

      <h2>1. Identificación del responsable</h2>

      <p>
      La presente Política de Privacidad y Tratamiento de Datos Personales regula la recolección, uso, almacenamiento, circulación, supresión y demás formas de tratamiento de datos personales realizados por <strong>Kora, persona natural responsable del proyecto Kora Business Agents</strong>, con domicilio de operación en <strong>[CIUDAD, PAÍS]</strong>, en adelante “Kora”, “Kora Business Agents”, “el Servicio” o “nosotros”.
      </p>

      <p>
      Para efectos de esta política, el canal de contacto para consultas, reclamos, solicitudes de actualización, rectificación, supresión de datos o revocatoria de autorización es:
      </p>

      <p>
      <strong>Correo electrónico:</strong> {site.email}
      <strong>Sitio web:</strong> [URL DEL SITIO WEB]
      </p>

      <h2>2. Marco legal aplicable</h2>

      <p>
      Esta política se adopta en cumplimiento de la Constitución Política de Colombia, la Ley 1581 de 2012, el Decreto 1377 de 2013, el Decreto Único Reglamentario 1074 de 2015, las instrucciones de la Superintendencia de Industria y Comercio y las demás normas que las modifiquen, adicionen o sustituyan.
      </p>

      <h2>3. Ámbito de aplicación</h2>

      <p>
      Esta política aplica al tratamiento de datos personales realizado por Kora Business Agents en el desarrollo de sus actividades tecnológicas, comerciales, operativas y de soporte, incluyendo el uso de agentes digitales, automatización conversacional, integraciones con WhatsApp Business Platform, calendarios digitales, formularios web, canales de soporte, herramientas de analítica operativa y otros medios electrónicos.
      </p>

      <p>
      Cuando Kora Business Agents trate datos personales por cuenta de una empresa cliente, clínica, consultorio, profesional independiente u otra organización, podrá actuar como encargado del tratamiento, siguiendo las instrucciones del respectivo responsable. Cuando Kora Business Agents determine directamente las finalidades y medios del tratamiento, actuará como responsable del tratamiento.
      </p>

      <h2>4. Datos personales que podemos tratar</h2>

      <p>
      En desarrollo del Servicio, podemos recolectar y tratar las siguientes categorías de datos personales:
      </p>

      <ul>
        <li>Datos de identificación, como nombre, apellido, tipo y número de documento, cuando sean proporcionados por el titular.</li>
        <li>Datos de contacto, como número de teléfono, correo electrónico, ciudad o país.</li>
        <li>Datos asociados a conversaciones por canales digitales, incluyendo mensajes enviados por WhatsApp, respuestas automatizadas, solicitudes realizadas, fecha y hora de la conversación y estado de la atención.</li>
        <li>Datos necesarios para la gestión de citas o servicios, como tipo de servicio solicitado, fecha, hora, profesional, sede, observaciones y estado de la reserva.</li>
        <li>Datos técnicos básicos, como identificadores de mensaje, registros de eventos, logs de sistema, metadatos operativos y datos necesarios para seguridad, auditoría y funcionamiento del Servicio.</li>
        <li>Datos comerciales o de relación con clientes, como historial de interacciones, solicitudes de información, cotizaciones, acuerdos, comunicaciones relacionadas con el Servicio y soporte prestado.</li>
      </ul>

      <h2>5. Datos sensibles</h2>

      <p>
      En algunos casos, especialmente cuando el Servicio sea utilizado por clínicas, consultorios, profesionales de salud u organizaciones similares, las conversaciones podrían incluir información relacionada con salud, tratamientos, síntomas, procedimientos, citas médicas u otra información que pueda considerarse dato sensible conforme a la legislación colombiana.
      </p>

      <p>
      El suministro de datos sensibles es facultativo. El titular no está obligado a entregar información sensible si no desea hacerlo. Cuando sea necesario tratar datos sensibles, dicho tratamiento se realizará únicamente cuando exista autorización expresa, previa e informada del titular, cuando sea necesario para la prestación del servicio solicitado, o cuando exista una base legal que lo permita.
      </p>

      <p>
      Kora Business Agents no solicita información sensible que no sea necesaria para gestionar la solicitud del usuario. Recomendamos a los usuarios no compartir información médica, financiera, familiar, íntima o especialmente protegida salvo que sea estrictamente necesaria para la atención solicitada.
      </p>

      <h2>6. Tratamiento de datos de niños, niñas y adolescentes</h2>

      <p>
      El Servicio no está dirigido directamente a niños, niñas o adolescentes. En caso de que se traten datos personales de menores de edad, dicho tratamiento se realizará respetando sus derechos prevalentes y, cuando corresponda, con la autorización de sus padres, representantes legales o acudientes, conforme a la normativa colombiana aplicable.
      </p>

      <h2>7. Finalidades del tratamiento</h2>

      <p>
      Los datos personales podrán ser tratados para las siguientes finalidades:
      </p>

      <ul>
        <li>Responder consultas, solicitudes o mensajes enviados por los usuarios a través de WhatsApp u otros canales digitales.</li>
        <li>Gestionar solicitudes de información, reservas, cancelaciones, reprogramaciones o confirmaciones de citas.</li>
        <li>Automatizar la atención inicial de usuarios, clientes o pacientes mediante agentes conversacionales.</li>
        <li>Enviar confirmaciones, recordatorios, respuestas operativas y comunicaciones relacionadas con el servicio solicitado.</li>
        <li>Registrar el historial mínimo necesario de conversaciones para continuidad de la atención, auditoría, soporte y mejora del Servicio.</li>
        <li>Integrar el Servicio con herramientas tecnológicas como calendarios digitales, sistemas de mensajería, bases de datos, herramientas de analítica operativa o plataformas cloud.</li>
        <li>Prestar soporte técnico, resolver incidencias, verificar funcionamiento del sistema y prevenir errores, fraude, abuso o accesos no autorizados.</li>
        <li>Cumplir obligaciones legales, contractuales, contables, administrativas o requerimientos de autoridades competentes.</li>
        <li>Realizar actividades comerciales, administrativas o de relacionamiento con clientes actuales o potenciales, siempre dentro del marco legal aplicable.</li>
        <li>Mejorar productos, servicios, modelos de atención, procesos internos y experiencia de usuario.</li>
      </ul>

      <h2>8. Autorización del titular</h2>

      <p>
      Al interactuar con nuestros canales digitales, enviar información mediante WhatsApp, formularios, correo electrónico u otros medios, el titular autoriza el tratamiento de sus datos personales conforme a esta política, siempre que dicha autorización sea requerida por la ley.
      </p>

      <p>
      Cuando Kora Business Agents actúe como encargado del tratamiento por cuenta de un cliente empresarial, el responsable del tratamiento será quien deba obtener las autorizaciones correspondientes de los titulares, sin perjuicio de las obligaciones que le correspondan a Kora Business Agents como encargado.
      </p>

      <h2>9. Derechos de los titulares</h2>

      <p>
      De acuerdo con la legislación colombiana sobre protección de datos personales, los titulares tienen derecho a:
      </p>

      <ul>
        <li>Conocer, actualizar y rectificar sus datos personales.</li>
        <li>Solicitar prueba de la autorización otorgada para el tratamiento, cuando dicha autorización sea requerida.</li>
        <li>Ser informados sobre el uso que se ha dado a sus datos personales.</li>
        <li>Presentar consultas y reclamos relacionados con el tratamiento de sus datos.</li>
        <li>Solicitar la supresión de sus datos personales cuando sea procedente.</li>
        <li>Revocar la autorización otorgada para el tratamiento, cuando no exista un deber legal o contractual que impida la eliminación de los datos.</li>
        <li>Acceder gratuitamente a sus datos personales en los términos previstos por la ley.</li>
        <li>Presentar quejas ante la Superintendencia de Industria y Comercio cuando considere que se ha vulnerado su derecho de habeas data, previo agotamiento del trámite de consulta o reclamo ante el responsable o encargado, cuando corresponda.</li>
      </ul>

      <h2>10. Procedimiento para consultas, reclamos y solicitudes</h2>

      <p>
      El titular puede ejercer sus derechos enviando una solicitud al correo electrónico <strong>{site.email}</strong>.
      </p>

      <p>
      La solicitud deberá incluir, como mínimo:
      </p>

      <ul>
        <li>Nombre completo del titular.</li>
        <li>Número de identificación, si aplica.</li>
        <li>Número de teléfono o correo asociado a la información solicitada.</li>
        <li>Descripción clara de la consulta, reclamo o solicitud.</li>
        <li>Documentos que acrediten la identidad del titular o la representación, cuando aplique.</li>
      </ul>

      <p>
      Las consultas y reclamos serán atendidos dentro de los términos establecidos por la normativa colombiana aplicable. Cuando no sea posible atender la solicitud dentro del término inicial, se informará al solicitante los motivos de la demora y la fecha estimada de respuesta.
      </p>

      <h2>11. Conservación de los datos</h2>

      <p>
      Los datos personales se conservarán durante el tiempo necesario para cumplir las finalidades para las cuales fueron recolectados, prestar el servicio solicitado, mantener registros operativos, atender obligaciones legales o contractuales, resolver disputas, realizar auditorías y cumplir requerimientos de autoridades competentes.
      </p>

      <p>
      Una vez cumplida la finalidad del tratamiento y siempre que no exista obligación legal, contractual o técnica que exija su conservación, los datos serán eliminados, anonimizados o bloqueados conforme a los procedimientos internos aplicables.
      </p>

      <h2>12. Seguridad de la información</h2>

      <p>
      Kora Business Agents adopta medidas razonables de seguridad administrativas, técnicas y organizativas orientadas a proteger los datos personales contra acceso no autorizado, pérdida, uso indebido, alteración, divulgación o destrucción no autorizada.
      </p>

      <p>
      No obstante, ningún sistema tecnológico o transmisión de información por internet puede garantizar seguridad absoluta. El usuario reconoce que el uso de canales digitales implica ciertos riesgos inherentes.
      </p>

      <h2>13. Transferencia y transmisión de datos</h2>

      <p>
      Para cumplir las finalidades descritas en esta política, Kora Business Agents podrá compartir, transmitir o permitir el acceso a datos personales a proveedores tecnológicos, plataformas de mensajería, servicios de hosting, herramientas cloud, servicios de calendario, proveedores de soporte, aliados operativos, clientes empresariales o autoridades competentes, cuando sea necesario y permitido por la ley.
      </p>

      <p>
      Algunos proveedores tecnológicos pueden estar ubicados fuera de Colombia. En esos casos, Kora Business Agents procurará adoptar medidas razonables para que el tratamiento de los datos se realice conforme a estándares adecuados de seguridad, confidencialidad y protección de datos.
      </p>

      <h2>14. Uso de WhatsApp Business Platform y servicios de terceros</h2>

      <p>
      El Servicio puede operar mediante WhatsApp Business Platform, APIs de Meta, herramientas de calendario, servicios cloud y otras plataformas tecnológicas de terceros. El uso de dichos canales puede estar sujeto también a las políticas, condiciones y prácticas de privacidad de esos terceros.
      </p>

      <p>
      Kora Business Agents no controla completamente la infraestructura, políticas o decisiones técnicas de dichas plataformas externas. Por ello, recomendamos a los usuarios revisar las políticas de privacidad de WhatsApp, Meta y demás servicios utilizados.
      </p>

      <h2>15. Comunicaciones comerciales</h2>

      <p>
      Kora Business Agents podrá enviar comunicaciones comerciales, informativas o promocionales únicamente cuando cuente con autorización para ello o exista una base legal que lo permita. El titular podrá solicitar en cualquier momento dejar de recibir comunicaciones comerciales no esenciales.
      </p>

      <h2>16. Limitación sobre servicios de salud y emergencias</h2>

      <p>
      Los agentes conversacionales de Kora Business Agents pueden ayudar a gestionar información, citas, recordatorios y atención inicial, pero no sustituyen el criterio médico, odontológico, psicológico o profesional. En caso de urgencia médica o situación que requiera atención inmediata, el usuario debe contactar directamente a los servicios de emergencia, acudir a un centro asistencial o comunicarse con un profesional autorizado.
      </p>

      <h2>17. Modificaciones de la política</h2>

      <p>
      Kora Business Agents podrá modificar esta Política de Privacidad y Tratamiento de Datos Personales en cualquier momento. Las modificaciones serán publicadas en este sitio web y, cuando sean sustanciales, se informarán por los medios que resulten razonables según el tipo de relación con el titular.
      </p>

      <h2>18. Vigencia</h2>

      <p>
      Esta política rige a partir del 4 de junio de 2026 y permanecerá vigente mientras Kora Business Agents realice tratamiento de datos personales en desarrollo de sus actividades.
      </p>
    </LegalPageLayout>
  )
}
