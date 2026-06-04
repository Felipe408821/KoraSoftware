import { Link } from 'react-router-dom'

// Botón polimórfico: se renderiza como <button>, <a> o <Link> según las props.
// - to="/ruta"      -> React Router <Link>
// - href="..."      -> <a> (mailto, anclas, externos)
// - sin to/href     -> <button>
const variants = {
  primary:
    'bg-brand-gradient text-white shadow-glow hover:shadow-card hover:-translate-y-0.5 focus-visible:ring-brand-500',
  secondary:
    'bg-white text-ink border border-ink/10 hover:border-brand-300 hover:text-brand-700 hover:-translate-y-0.5 focus-visible:ring-brand-400',
  ghost:
    'bg-transparent text-ink-soft hover:text-brand-700 hover:bg-brand-50 focus-visible:ring-brand-300',
}

const sizes = {
  sm: 'px-4 py-2 text-sm',
  md: 'px-5 py-2.5 text-sm',
  lg: 'px-6 py-3 text-base',
}

export default function Button({
  children,
  variant = 'primary',
  size = 'md',
  to,
  href,
  className = '',
  ...props
}) {
  const base =
    'inline-flex items-center justify-center gap-2 rounded-full font-semibold transition-all duration-200 ease-out outline-none focus-visible:ring-2 focus-visible:ring-offset-2'
  const classes = `${base} ${variants[variant]} ${sizes[size]} ${className}`

  if (to) {
    return (
      <Link to={to} className={classes} {...props}>
        {children}
      </Link>
    )
  }

  if (href) {
    const isExternal = href.startsWith('http')
    return (
      <a
        href={href}
        className={classes}
        {...(isExternal ? { target: '_blank', rel: 'noreferrer noopener' } : {})}
        {...props}
      >
        {children}
      </a>
    )
  }

  return (
    <button className={classes} {...props}>
      {children}
    </button>
  )
}
