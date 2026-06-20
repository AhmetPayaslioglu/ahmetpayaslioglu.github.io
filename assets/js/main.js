// Mobile nav toggle
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', () => links.classList.toggle('open'));
  }

  // Language switch: persist manual choice
  document.querySelectorAll('.lang-switch a').forEach(a => {
    a.addEventListener('click', () => {
      const lang = a.dataset.lang;
      if (lang) localStorage.setItem('lang', lang);
    });
  });

  // Auto language detection — runs once per session
  autoLanguageRedirect();
});

async function autoLanguageRedirect() {
  // Already evaluated this session — bail to avoid loops
  if (sessionStorage.getItem('lang-evaluated')) return;
  sessionStorage.setItem('lang-evaluated', '1');

  // Manual choice always wins
  const saved = localStorage.getItem('lang');
  let preferred = saved;

  if (!preferred) {
    preferred = await detectPreferredLang();
  }

  const currentLang = document.documentElement.lang;
  if (preferred && preferred !== currentLang) {
    const altLink = document.querySelector(`link[rel="alternate"][hreflang="${preferred}"]`);
    if (altLink && altLink.href) {
      window.location.replace(altLink.href);
    }
  }
}

async function detectPreferredLang() {
  // Try IP geolocation (most accurate)
  try {
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), 1500);
    const resp = await fetch('https://ipapi.co/country/', { signal: ctrl.signal });
    clearTimeout(timer);
    if (resp.ok) {
      const country = (await resp.text()).trim().toUpperCase();
      if (country === 'TR') return 'tr';
      if (country.length === 2) return 'en';
    }
  } catch (_) {
    // fall through to browser-language fallback
  }

  // Fallback: browser language
  const browserLang = (navigator.language || '').toLowerCase();
  return browserLang.startsWith('tr') ? 'tr' : 'en';
}
