
document.addEventListener("DOMContentLoaded", () => {
  const header = document.querySelector(".md-header__title");
  if (header) {
    header.setAttribute("data-version", "{{ project_version }}");
  }
});
