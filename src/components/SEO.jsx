import { useEffect } from 'react'
import { site } from '../config/site.js'

// Actualiza el <title> y la meta description (y OG) al montar la página.
// Sin dependencias externas: manipula el DOM directamente.
function setMeta(attr, key, content) {
  if (!content) return
  let el = document.head.querySelector(`meta[${attr}="${key}"]`)
  if (!el) {
    el = document.createElement('meta')
    el.setAttribute(attr, key)
    document.head.appendChild(el)
  }
  el.setAttribute('content', content)
}

export default function SEO({ title, description }) {
  useEffect(() => {
    const fullTitle = title ? `${title} · ${site.brand}` : `${site.brand}`
    document.title = fullTitle

    if (description) {
      setMeta('name', 'description', description)
      setMeta('property', 'og:description', description)
      setMeta('name', 'twitter:description', description)
    }
    setMeta('property', 'og:title', fullTitle)
    setMeta('name', 'twitter:title', fullTitle)
  }, [title, description])

  return null
}
