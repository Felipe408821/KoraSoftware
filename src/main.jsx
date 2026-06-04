import React from 'react'
import ReactDOM from 'react-dom/client'
import { HashRouter } from 'react-router-dom'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/*
      Usamos HashRouter para que el routing funcione en GitHub Pages sin
      configurar redirecciones 404 ni la ruta base del repositorio.
      Las rutas quedan como /#/privacy-policy, /#/data-deletion, etc.
    */}
    <HashRouter>
      <App />
    </HashRouter>
  </React.StrictMode>,
)
