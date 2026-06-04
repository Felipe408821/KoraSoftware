import { useState } from 'react'
import Button from './Button.jsx'
import { site, mailtoLink, whatsappLink } from '../config/site.js'
import { IconArrowRight, IconChat } from './icons.jsx'

const fields = [
  { name: 'nombre', label: 'Nombre', type: 'text', required: true, placeholder: 'Tu nombre' },
  { name: 'empresa', label: 'Empresa / clínica', type: 'text', placeholder: 'Nombre de tu negocio' },
  { name: 'email', label: 'Email', type: 'email', required: true, placeholder: 'tu@email.com' },
  { name: 'telefono', label: 'Teléfono', type: 'tel', placeholder: '+34 600 000 000' },
]

// Formulario estático: al enviar, compone un mailto con todos los campos.
// No hay backend; queda preparado para integrar uno en el futuro.
export default function ContactForm() {
  const [values, setValues] = useState({
    nombre: '',
    empresa: '',
    email: '',
    telefono: '',
    mensaje: '',
  })

  const update = (name) => (e) => setValues((v) => ({ ...v, [name]: e.target.value }))

  const handleSubmit = (e) => {
    e.preventDefault()
    const body =
      `Nombre: ${values.nombre}\n` +
      `Empresa / clínica: ${values.empresa}\n` +
      `Email: ${values.email}\n` +
      `Teléfono: ${values.telefono}\n\n` +
      `Mensaje:\n${values.mensaje}\n`
    window.location.href = mailtoLink({
      subject: `Contacto / demo — ${values.nombre || 'Kora Software'}`,
      body,
    })
  }

  const wa = whatsappLink()

  return (
    <form onSubmit={handleSubmit} className="card-ring p-6 sm:p-8">
      <div className="grid gap-4 sm:grid-cols-2">
        {fields.map((f) => (
          <div key={f.name} className={f.name === 'mensaje' ? 'sm:col-span-2' : ''}>
            <label htmlFor={f.name} className="mb-1.5 block text-sm font-medium text-ink-soft">
              {f.label} {f.required && <span className="text-brand-500">*</span>}
            </label>
            <input
              id={f.name}
              name={f.name}
              type={f.type}
              required={f.required}
              placeholder={f.placeholder}
              value={values[f.name]}
              onChange={update(f.name)}
              className="w-full rounded-xl border border-ink/10 bg-white px-4 py-2.5 text-sm text-ink shadow-sm outline-none transition focus:border-brand-400 focus:ring-2 focus:ring-brand-100"
            />
          </div>
        ))}

        <div className="sm:col-span-2">
          <label htmlFor="mensaje" className="mb-1.5 block text-sm font-medium text-ink-soft">
            Mensaje
          </label>
          <textarea
            id="mensaje"
            name="mensaje"
            rows={4}
            placeholder="Cuéntanos qué te gustaría automatizar…"
            value={values.mensaje}
            onChange={update('mensaje')}
            className="w-full resize-y rounded-xl border border-ink/10 bg-white px-4 py-2.5 text-sm text-ink shadow-sm outline-none transition focus:border-brand-400 focus:ring-2 focus:ring-brand-100"
          />
        </div>
      </div>

      <div className="mt-6 flex flex-col gap-3 sm:flex-row sm:items-center">
        <Button type="submit" size="lg" className="w-full sm:w-auto">
          Enviar y solicitar demo
          <IconArrowRight width={18} height={18} />
        </Button>
        {wa && (
          <Button href={wa} variant="secondary" size="lg" className="w-full sm:w-auto">
            <IconChat width={18} height={18} />
            Escríbenos por WhatsApp
          </Button>
        )}
      </div>

      <p className="mt-4 text-xs text-ink-muted">
        Al enviar se abrirá tu cliente de correo con los datos rellenados. También
        puedes escribirnos directamente a{' '}
        <a href={`mailto:${site.email}`} className="font-medium text-brand-700 hover:underline">
          {site.email}
        </a>
        .
      </p>
    </form>
  )
}
