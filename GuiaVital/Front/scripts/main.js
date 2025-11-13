// Carrega componentes HTML dinâmicos (header e footer)
async function loadComponent(id, path) {
  try {
    const response = await fetch(path);
    if (!response.ok) throw new Error(`Erro ${response.status}: ${path}`);
    const html = await response.text();
    document.getElementById(id).innerHTML = html;
  } catch (err) {
    console.error("Erro ao carregar componente:", err);
  }
}

// Ao carregar a página
document.addEventListener("DOMContentLoaded", async () => {
  await loadComponent("header", "components/header.html");
  await loadComponent("footer", "components/footer.html");
});

// Tema claro/escuro
function toggleTheme() {
  const html = document.documentElement;
  const current = html.getAttribute("data-theme");
  const next = current === "light" ? "dark" : "light";
  html.setAttribute("data-theme", next);
  localStorage.setItem("theme", next);
}

// Carregar tema salvo
window.addEventListener("load", () => {
  const theme = localStorage.getItem("theme") || "light";
  document.documentElement.setAttribute("data-theme", theme);
});

// Sidebar
function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  sidebar.classList.toggle("-translate-x-full");
}
