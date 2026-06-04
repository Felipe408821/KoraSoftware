// Tarjeta de característica/beneficio con icono, título y descripción.
// El icono se pasa como nodo (SVG) en la prop `icon`.
export default function FeatureCard({ icon, title, description, className = '' }) {
  return (
    <div
      className={`group card-ring h-full p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-card ${className}`}
    >
      {icon && (
        <div className="mb-5 inline-flex h-11 w-11 items-center justify-center rounded-2xl bg-brand-gradient-soft text-brand-600 ring-1 ring-brand-100 transition-colors group-hover:text-brand-700">
          {icon}
        </div>
      )}
      <h3 className="text-base font-semibold text-ink">{title}</h3>
      {description && (
        <p className="mt-2 text-[15px] leading-relaxed text-ink-muted">{description}</p>
      )}
    </div>
  )
}
