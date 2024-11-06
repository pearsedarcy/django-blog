// theme-toggle.js

// Get the theme toggle checkbox
const themeToggle = document.querySelector(".theme-controller");

// Check the saved theme in localStorage
const savedTheme = localStorage.getItem("theme");
if (savedTheme) {
  document.documentElement.setAttribute("data-theme", savedTheme);
  themeToggle.checked = savedTheme === "forest"; // Assuming you want to toggle between "synthwave" and "dracula"
} else {
  // Default theme
  document.documentElement.setAttribute("data-theme", "dracula");
}

themeToggle.addEventListener("change", (event) => {
  const theme = event.target.checked ? "forest" : "dracula";
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("theme", theme); // Save the selected theme to localStorage
});
