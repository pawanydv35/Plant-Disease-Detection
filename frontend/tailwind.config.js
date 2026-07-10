/** @type {import('tailwindcss').Config} */
export default {
  darkMode: "class",
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        background: "#FAFAF7",
        surface: "#EEF3EA",
        forest: {
          DEFAULT: "#2F6B4F",
          dark: "#234F3A",
          light: "#3E8763",
        },
        moss: "#6B9B3F",
        charcoal: "#1C2321",
        rust: "#C1502E",
      },
      fontFamily: {
        display: ["Fraunces", "serif"],
        body: ["Inter", "sans-serif"],
        mono: ["IBM Plex Mono", "monospace"],
      },
      borderRadius: {
        xl: "1rem",
        "2xl": "1.5rem",
      },
      keyframes: {
        scan: {
          "0%": { transform: "translateY(-100%)" },
          "100%": { transform: "translateY(100%)" },
        },
      },
      animation: {
        scan: "scan 1.8s ease-in-out infinite",
      },
    },
  },
  plugins: [],
};
