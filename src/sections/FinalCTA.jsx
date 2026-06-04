import Reveal from '../components/Reveal.jsx'
import Button from '../components/Button.jsx'
import { demoMailto } from '../config/site.js'
import { IconArrowRight } from '../components/icons.jsx'

export default function FinalCTA() {
  return (
    <section className="py-20 sm:py-28">
      <div className="container-kora">
        <Reveal>
          <div className="relative overflow-hidden rounded-4xl bg-ink px-6 py-16 text-center sm:px-12 sm:py-20">
            {/* Decoración de fondo */}
            <div aria-hidden="true" className="pointer-events-none absolute inset-0">
              <div className="absolute inset-0 bg-brand-gradient opacity-90" />
              <div className="absolute -right-20 -top-20 h-72 w-72 rounded-full bg-white/15 blur-3xl" />
              <div className="absolute -bottom-24 -left-16 h-72 w-72 rounded-full bg-cyanx-400/30 blur-3xl" />
            </div>

            <div className="relative mx-auto max-w-2xl">
              <h2 className="text-3xl font-bold tracking-tight text-white sm:text-4xl md:text-[2.6rem] md:leading-[1.12]">
                Convierte WhatsApp en un canal de atención inteligente
              </h2>
              <p className="mt-5 text-lg leading-relaxed text-white/85">
                Solicita una demo y descubre cómo Kora puede ayudarte a
                automatizar conversaciones, citas y tareas repetitivas.
              </p>
              <div className="mt-9 flex justify-center">
                <Button
                  href={demoMailto}
                  variant="secondary"
                  size="lg"
                  className="!bg-white !text-brand-700 hover:!text-brand-800"
                >
                  Solicitar demo
                  <IconArrowRight width={18} height={18} />
                </Button>
              </div>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  )
}
