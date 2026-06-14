/** Expandable changelog cards for deal movement log. */
(function () {
  function init() {
    document.querySelectorAll(".changelog-card-header").forEach((btn) => {
      btn.addEventListener("click", () => {
        const card = btn.closest(".changelog-card");
        const body = card.querySelector(".changelog-body");
        const toggle = btn.querySelector(".changelog-toggle");
        const open = btn.getAttribute("aria-expanded") === "true";
        btn.setAttribute("aria-expanded", open ? "false" : "true");
        body.hidden = open;
        card.classList.toggle("expanded", !open);
        if (toggle) toggle.textContent = open ? "+" : "−";
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
