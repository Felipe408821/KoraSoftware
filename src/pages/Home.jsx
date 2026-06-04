import SEO from '../components/SEO.jsx'
import Hero from '../sections/Hero.jsx'
import Problem from '../sections/Problem.jsx'
import Solution from '../sections/Solution.jsx'
import HowItWorks from '../sections/HowItWorks.jsx'
import Benefits from '../sections/Benefits.jsx'
import UseCaseDental from '../sections/UseCaseDental.jsx'
import FutureUseCases from '../sections/FutureUseCases.jsx'
import Security from '../sections/Security.jsx'
import FinalCTA from '../sections/FinalCTA.jsx'
import ContactSection from '../sections/ContactSection.jsx'

export default function Home() {
  return (
    <>
      <SEO
        title="Agentes de IA para tu atención por WhatsApp"
        description="Kora Software ayuda a clínicas y negocios de servicios a responder clientes, gestionar citas y reducir tareas administrativas con agentes de IA disponibles 24/7."
      />
      <Hero />
      <Problem />
      <Solution />
      <HowItWorks />
      <Benefits />
      <UseCaseDental />
      <FutureUseCases />
      <Security />
      <FinalCTA />
      <ContactSection />
    </>
  )
}
