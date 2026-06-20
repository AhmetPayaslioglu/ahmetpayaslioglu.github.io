// Mobile nav toggle
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', () => links.classList.toggle('open'));
  }

  // Language preference persistence
  const langLinks = document.querySelectorAll('.lang-switch a');
  langLinks.forEach(a => {
    a.addEventListener('click', () => {
      const lang = a.dataset.lang;
      if (lang) localStorage.setItem('lang', lang);
    });
  });

  // Auto-redirect first-time visitors based on saved preference
  const saved = localStorage.getItem('lang');
  const currentLang = document.documentElement.lang;
  const altLink = document.querySelector(`link[rel="alternate"][hreflang="${saved}"]`);
  if (saved && currentLang !== saved && altLink && !sessionStorage.getItem('lang-redirected')) {
    sessionStorage.setItem('lang-redirected', '1');
    window.location.href = altLink.href;
  }
});
