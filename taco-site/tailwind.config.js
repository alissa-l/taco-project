/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './*.html',
    './src/**/*.vue',
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: '1rem',
        sm: '2rem',
        lg: '4rem',
        xl: '5rem',
        '2xl': '6rem',
      },
    },
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

