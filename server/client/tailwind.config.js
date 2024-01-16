/** @type {import('tailwindcss').Config} */
import colors from 'tailwindcss/colors'

export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}"
  ],
  theme: {
    extend: {},
    colors: {
      black: colors.black,
      blue: colors.blue,
      white: colors.white,
      gray: colors.gray,
      slate: colors.slate,
      indigo: colors.indigo,
    }
  },
  plugins: [],
}

