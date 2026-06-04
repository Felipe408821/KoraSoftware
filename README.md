# Kora Software — Sitio web

Sitio web corporativo de **Kora Software** (parte de **Kora Group**), producto
**KoraBusinessAgents**: agentes de IA para automatizar la atención al cliente, la
gestión de citas y las respuestas por canales digitales como WhatsApp.

Construido como sitio **estático** (sin backend), listo para desplegar gratis en
**GitHub Pages**.

---

## 🧱 Stack técnico

- **React 18** + **Vite 5**
- **Tailwind CSS 3**
- **React Router 6** (`HashRouter`, compatible con GitHub Pages sin configuración extra)
- Sin backend · sin dependencias innecesarias
- Animaciones discretas con CSS + `IntersectionObserver`
- Formularios con `mailto:` (y enlace opcional a WhatsApp)

---

## 📁 Estructura del proyecto

```
KoraSoftware/
├── index.html                # SEO base (title, description, Open Graph)
├── vite.config.js            # base: './' para GitHub Pages
├── tailwind.config.js        # paleta de marca, sombras, animaciones
├── postcss.config.js
├── public/
│   ├── favicon.svg
│   ├── og-image.svg          # imagen para redes (Open Graph)
│   └── .nojekyll
├── .github/workflows/
│   └── deploy.yml            # despliegue automático (opcional)
└── src/
    ├── main.jsx              # punto de entrada + HashRouter
    ├── App.jsx               # rutas + ScrollToTop
    ├── index.css             # Tailwind + estilos base + legal-prose
    ├── config/
    │   └── site.js           # ⭐ datos de empresa (email, dominio, etc.)
    ├── components/
    │   ├── Layout.jsx        # Navbar + Outlet + Footer
    │   ├── Navbar.jsx
    │   ├── Footer.jsx
    │   ├── Button.jsx        # botón polimórfico (button/a/Link)
    │   ├── Section.jsx
    │   ├── FeatureCard.jsx
    │   ├── LegalPageLayout.jsx
    │   ├── ChatMockup.jsx    # mockup de conversación (sin marca WhatsApp)
    │   ├── ContactForm.jsx
    │   ├── Reveal.jsx        # animación al hacer scroll
    │   ├── SEO.jsx           # title/meta por página
    │   ├── Logo.jsx
    │   └── icons.jsx         # set de iconos SVG
    ├── sections/             # secciones de la landing
    │   ├── Hero.jsx
    │   ├── Problem.jsx
    │   ├── Solution.jsx
    │   ├── HowItWorks.jsx
    │   ├── Benefits.jsx
    │   ├── UseCaseDental.jsx
    │   ├── FutureUseCases.jsx
    │   ├── Security.jsx
    │   ├── FinalCTA.jsx
    │   └── ContactSection.jsx
    └── pages/
        ├── Home.jsx
        ├── PrivacyPolicy.jsx
        ├── TermsAndConditions.jsx
        ├── DataDeletion.jsx       # bilingüe ES/EN (para revisión de Meta)
        ├── CookiesPolicy.jsx
        ├── Contact.jsx
        └── NotFound.jsx
```

---

## 🚀 Instalación y uso local

Requisitos: **Node 18+** y npm.

```bash
# 1. Instalar dependencias
npm install

# 2. Arrancar en modo desarrollo (http://localhost:5173)
npm run dev

# 3. Generar el build de producción (carpeta dist/)
npm run build

# 4. Previsualizar el build localmente
npm run preview
```

---

## 🌐 Rutas

| Ruta                        | Página                       |
| --------------------------- | ---------------------------- |
| `/`                         | Landing + contacto           |
| `/privacy-policy`           | Política de Privacidad       |
| `/terms-and-conditions`     | Términos y Condiciones       |
| `/data-deletion`            | Eliminación de Datos (ES/EN) |
| `/cookies-policy`           | Política de Cookies          |
| `/contact`                  | Contacto                     |

> Con `HashRouter`, las URLs reales incluyen `#`, por ejemplo:
> `https://usuario.github.io/kora-software/#/data-deletion`
> Esta es la URL que debes facilitar a Meta para «Data Deletion».

---

## 📦 Despliegue en GitHub Pages

Hay **dos formas**. Elige una.

### Opción A — Comando manual (`gh-pages`)

Ya incluida en el proyecto. Despliega la carpeta `dist` a la rama `gh-pages`.

```bash
# 1. Crea un repo en GitHub y enlázalo
git init
git add .
git commit -m "Kora Software website"
git branch -M main
git remote add origin https://github.com/USUARIO/REPO.git
git push -u origin main

# 2. Build + deploy
npm run deploy
```

Luego en GitHub: **Settings → Pages → Build and deployment → Source: _Deploy from a
branch_ → Branch: `gh-pages` / `(root)`**.

El sitio quedará en `https://USUARIO.github.io/REPO/`.

### Opción B — GitHub Actions (automático)

Incluido en `.github/workflows/deploy.yml`. Despliega solo con hacer `push` a `main`.

1. En GitHub: **Settings → Pages → Build and deployment → Source: _GitHub Actions_**.
2. Haz `git push` a `main`. El workflow construye y publica automáticamente.

> Gracias a `base: './'` en `vite.config.js` y a `HashRouter`, **no necesitas
> configurar el nombre del repositorio**: funciona bajo cualquier subruta.

---

## ⚙️ Personalización rápida

Casi todo lo editable está centralizado en **[`src/config/site.js`](src/config/site.js)**:

```js
export const site = {
  brand: 'Kora Software',
  email: 'contact@korasoftware.ai',  // ← cambia el email aquí
  whatsapp: '',                       // ← pon el número (34600000000) para activar el botón
  domain: 'https://korasoftware.ai',  // ← dominio cuando lo tengas
  country: 'España',
  legalEffectiveDate: '4 de junio de 2026',
  copyrightYear: 2026,
}
```

- **Email**: cambia `email` y se actualiza en todo el sitio (footer, legales, formularios).
- **WhatsApp**: rellena `whatsapp` con el número internacional sin signos para mostrar los botones de WhatsApp.
- **Colores de marca**: en `tailwind.config.js` (`brand`, `violetx`, `cyanx`).

---

## ✅ Recomendaciones finales (antes de producción)

1. **Revisión legal**: los textos de privacidad, términos, cookies y eliminación de
   datos son **plantillas orientativas**. Deben ser revisados y adaptados por un
   profesional jurídico según la actividad real y la normativa aplicable (RGPD/LOPDGDD).
2. **Email definitivo**: sustituye `contact@korasoftware.ai` por el correo real
   (idealmente uno monitorizado para solicitudes de eliminación de datos).
3. **Nombre legal de la empresa**: añade la razón social, NIF/CIF y domicilio en los
   documentos legales cuando estén disponibles.
4. **Dominio propio**: al contratar dominio, actualiza `domain` en `site.js`, las URLs
   `canonical`/Open Graph en `index.html` y configura el dominio en GitHub Pages
   (Settings → Pages → Custom domain) + un fichero `CNAME`.
5. **URL para Meta**: usa la URL completa de `/#/data-deletion` en la configuración de
   tu app de Meta / WhatsApp Business Platform.
6. **Imagen OG**: `public/og-image.svg` es un placeholder; si una red social no lee SVG,
   exporta una versión `.png` (1200×630) y actualiza las metaetiquetas en `index.html`.
7. **Analítica/cookies**: si añades analytics en el futuro, actualiza la Política de
   Cookies y añade el banner de consentimiento correspondiente.

---

## ⚖️ Avisos

- Kora Software **no está afiliada a WhatsApp ni a Meta**. «WhatsApp» se usa solo de
  forma descriptiva. No se utilizan logos oficiales de WhatsApp/Meta.
- Se evitan afirmaciones legales absolutas (p. ej. «100% compliant») y certificaciones
  no acreditadas.

© 2026 Kora Software. All rights reserved.
