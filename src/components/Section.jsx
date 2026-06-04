import Reveal from './Reveal.jsx'

// Contenedor de sección con encabezado opcional (eyebrow + título + subtítulo).
export default function Section({
  id,
  eyebrow,
  title,
  subtitle,
  align = 'center',
  className = '',
  containerClassName = '',
  children,
}) {
  const alignment = align === 'center' ? 'text-center mx-auto' : 'text-left'

  return (
    <section id={id} className={`py-20 sm:py-28 ${className}`}>
      <div className={`container-kora ${containerClassName}`}>
        {(eyebrow || title || subtitle) && (
          <Reveal className={`max-w-3xl ${alignment}`}>
            {eyebrow && <span className="eyebrow mb-5">{eyebrow}</span>}
            {title && (
              <h2 className="mt-5 text-3xl font-bold tracking-tight text-ink sm:text-4xl md:text-[2.6rem] md:leading-[1.1]">
                {title}
              </h2>
            )}
            {subtitle && (
              <p className="mt-5 text-lg leading-relaxed text-ink-muted">{subtitle}</p>
            )}
          </Reveal>
        )}
        {children}
      </div>
    </section>
  )
}
