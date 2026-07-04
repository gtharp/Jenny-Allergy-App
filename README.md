# Jenny Allergy App

Daily pollen & allergen alerts for Jenny in San Antonio, TX — delivered straight to her inbox.

> **Goal:** Every morning (≈ 6 AM CDT) Jenny receives a concise email telling her whether cedar, ragweed, or mold spores are going to ruin the day.

**Live demo:** https://gtharp.github.io/Jenny-Allergy-App/  
*(auto-published from `main` via GitHub Pages)*

---

## What’s new (v 0.3 — 2025-07-11)

- **GitHub Pages enabled** – `_config.yml` now configures a minimal Jekyll theme, so pushes to `main` publish automatically. ([GitHub](https://github.com/gtharp/Jenny-Allergy-App))
- **Timestamp injection** – `index.html` adds a JS hook that prints the exact build time, so Jenny knows when the data was generated. ([GitHub](https://github.com/gtharp/Jenny-Allergy-App))
- **Style refresh** – `styles.css` cleaned up: renamed CSS variables, better mobile spacing, and dark-mode-friendly contrast tweaks. ([GitHub](https://github.com/gtharp/Jenny-Allergy-App))

---

## Current status

Prototype **v 0.3** – still a static front-end, but everything is wired for back-end work.

| Done | Feature |
|---|---|
|✅|Semantic landing page with automatic *today* date and “last updated” timestamp|
|✅|Responsive, accessible styling with color-coded pollen severity pills|
|✅|GitHub Pages deployment via `_config.yml`|
|✅|Pollen-API integration|
|✅|Daily pollen email via GitHub Action|
|🚧|Multi-user support|

---

## Roadmap

| Stage | Tasks | Target |
|---|---|---|
|**MVP – Automated Email**|Fetch daily pollen forecast (Tomorrow.io) → format & send via email; store secrets in repo settings|v 1.0|
|**Dashboard – Live Site**|Replace static text with live fetch; 7-day history chart (Recharts); add PWA manifest|v 1.1|
|**Polish & Growth**|Retry/alert logic on API failure; multi-user support; Cypress tests; Plausible analytics|v 1.2 +|

---

## Tech stack (planned)

* **Frontend:** vanilla HTML / CSS / JS (no frameworks)  
* **Data:** Tomorrow.io pollen API  
* **Messaging:** Email (SMTP)  
* **Automation:** GitHub Actions daily cron  
* **Hosting:** GitHub Pages (Jekyll minimal theme)

---

## Local development


# Clone
git clone https://github.com/gtharp/Jenny-Allergy-App.git
cd Jenny-Allergy-App

# Static prototype (v0.3)
open index.html    # or just double-click it


### When the backend is ready


pip install -r requirements.txt
export POLLEN_API_KEY=... EMAIL_ADDRESS=... EMAIL_APP_PASSWORD=... JENNY_EMAIL=...
python src/pollen_email.py


---

## Contributing

Pull requests are welcome! Please open an issue first to discuss any major changes.

## License

MIT — see `LICENSE` for details.

Feel free to tweak the wording or add badges, but this should cover the new deployment setup and UI updates while keeping the roadmap intact.
