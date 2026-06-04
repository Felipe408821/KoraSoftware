/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        // Texto y fondos
        ink: {
          DEFAULT: '#0b1020', // azul muy oscuro (texto principal)
          soft: '#1c2540',
          muted: '#5b6478',
        },
        // Color primario: azul profundo
        brand: {
          50: '#eef2ff',
          100: '#e0e7ff',
          200: '#c7d2fe',
          300: '#a5b4fc',
          400: '#818cf8',
          500: '#6366f1',
          600: '#4f46e5',
          700: '#4338ca',
          800: '#3730a3',
          900: '#312e81',
        },
        // Acento violeta tecnológico
        violetx: {
          400: '#a78bfa',
          500: '#8b5cf6',
          600: '#7c3aed',
        },
        // Acento cyan elegante
        cyanx: {
          400: '#22d3ee',
          500: '#06b6d4',
        },
      },
      fontFamily: {
        sans: [
          'Inter',
          'ui-sans-serif',
          'system-ui',
          '-apple-system',
          'Segoe UI',
          'Roboto',
          'Helvetica Neue',
          'Arial',
          'sans-serif',
        ],
      },
      borderRadius: {
        '4xl': '2rem',
      },
      boxShadow: {
        soft: '0 1px 3px rgba(11, 16, 32, 0.04), 0 12px 32px -12px rgba(11, 16, 32, 0.12)',
        card: '0 1px 2px rgba(11, 16, 32, 0.04), 0 18px 40px -20px rgba(79, 70, 229, 0.22)',
        glow: '0 20px 60px -20px rgba(99, 102, 241, 0.45)',
      },
      backgroundImage: {
        'brand-gradient': 'linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #06b6d4 100%)',
        'brand-gradient-soft':
          'linear-gradient(135deg, rgba(79,70,229,0.10) 0%, rgba(124,58,237,0.08) 50%, rgba(6,182,212,0.06) 100%)',
      },
      keyframes: {
        'fade-up': {
          '0%': { opacity: '0', transform: 'translateY(16px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-8px)' },
        },
        'pulse-soft': {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0.5' },
        },
      },
      animation: {
        'fade-up': 'fade-up 0.6s ease-out both',
        float: 'float 6s ease-in-out infinite',
        'pulse-soft': 'pulse-soft 1.4s ease-in-out infinite',
      },
    },
  },
  plugins: [],
}
