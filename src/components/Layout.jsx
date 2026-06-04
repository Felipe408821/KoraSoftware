import { Outlet } from 'react-router-dom'
import Navbar from './Navbar.jsx'
import Footer from './Footer.jsx'

// Layout compartido por todas las rutas: Navbar fija + contenido + Footer.
export default function Layout() {
  return (
    <div className="flex min-h-screen flex-col">
      <Navbar />
      <main className="flex-1 pt-16 sm:pt-18">
        <Outlet />
      </main>
      <Footer />
    </div>
  )
}
