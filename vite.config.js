import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
//
// `base: './'` genera rutas relativas para los assets, de modo que el sitio
// funciona tanto en local como en GitHub Pages bajo cualquier nombre de
// repositorio (p. ej. https://usuario.github.io/kora-software/) sin necesidad
// de configurar la ruta base. Combinado con HashRouter, el routing funciona
// sin trucos de redirección 404.
export default defineConfig({
  base: './KoraSoftware/',
  plugins: [react()],
})
