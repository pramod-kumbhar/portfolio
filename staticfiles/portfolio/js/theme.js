const root = document.documentElement;
const toggle = document.querySelector(".theme-toggle");
const savedTheme = localStorage.getItem("portfolio-theme");

if (savedTheme) {
  root.dataset.theme = savedTheme;
}

toggle?.addEventListener("click", () => {
  const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
  root.dataset.theme = nextTheme;
  localStorage.setItem("portfolio-theme", nextTheme);
});

const revealItems = document.querySelectorAll(".reveal");

if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.14 }
  );

  revealItems.forEach((item, index) => {
    item.style.transitionDelay = `${Math.min(index * 70, 420)}ms`;
    observer.observe(item);
  });
} else {
  revealItems.forEach((item) => item.classList.add("visible"));
}
