/** @type {import('tailwindcss').Config} */
export default {
  content: ["index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {},
  },
  fontFamily: {
    Roboto: ['Roboto', 'sans-serif'],
  },
  container: {
    center: true,
    padding: '1rem',
  },
  screens: {
    sm: '640px',
    md: '768px',
  },
  plugins: [],
}

