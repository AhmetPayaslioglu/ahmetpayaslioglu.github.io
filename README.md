# ahmetpayaslioglu.github.io

Personal site of Ahmet Payaslıoğlu — Senior Cyber Security Incident Responder (L3), Threat Hunter and Detection Engineer.

Static HTML/CSS/JS site hosted on GitHub Pages. Bilingual (TR / EN).

## Structure

```
/                    Turkish pages (index, hakkimda, hizmetler, egitimler, sertifikalar, iletisim)
/en/                 English pages (index, about, services, training, certificates, contact)
/assets/css/         Styles
/assets/js/          Client-side scripts (nav toggle, language persistence)
/assets/img/         Images
```

## Local preview

```
python -m http.server 8000
```

Open http://localhost:8000

## Notes

- `.nojekyll` disables Jekyll processing on GitHub Pages.
- Contact form uses Formspree — replace `your-form-id` in `iletisim.html` and `en/contact.html` with the real endpoint after creating a Formspree account.
- `CNAME` file is added when a custom domain is configured.
