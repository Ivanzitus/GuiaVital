// Importação dinâmica dos componentes
async function loadComponent(id, path) {
  const res = await fetch(path);
  const html = await res.text();
  document.getElementById(id).innerHTML = html;
}

// Carrega header e footer automaticamente
document.addEventListener("DOMContentLoaded", async () => {
  await loadComponent("header", "components/header.html");
  await loadComponent("footer", "components/footer.html");

  const savedTheme = localStorage.getItem("theme") || "synthwave";
  document.documentElement.setAttribute("data-theme", savedTheme);
  const checkbox = document.getElementById("themeToggle");
  if (checkbox) checkbox.checked = savedTheme !== "silk";
});

// Função de alternância do tema
function toggleTheme() {
  const checkbox = document.getElementById("themeToggle");
  const theme = checkbox.checked ? "synthwave" : "silk";
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("theme", theme);
}

// Abrir e fechar sidebar
function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  sidebar.classList.toggle("-translate-x-full");
}
