# Jenny Allergy App

Daily pollen & allergen alerts for **Jenny** in San Antonio, TX — delivered to her phone *and* rendered live on the site.

> **Goal:** At \~6 AM Central each day Jenny gets a quick heads‑up on cedar, ragweed, or mold so she can prep before heading out.

**Live demo:** [https://gtharp.github.io/Jenny-Allergy-App/](https://gtharp.github.io/Jenny-Allergy-App/)\
*(auto‑published from **``** via GitHub Pages)*

---

## What’s new (v 0.4 — 2025‑07‑12)

| 🔄 Change                 | Details                                                                                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Dynamic pollen fetch**  | `index.html` now hits Tomorrow\.io’s *Timelines* endpoint on every page load and maps the numeric `treeIndex` to **None / Low / Medium / High / Extreme** severity pills. |
| **Better error handling** | Bad key or missing CORS?  The UI prints a graceful “Error loading data.” and the console logs the exact HTTP code.                                                        |
| **Style harmony**         | Merged George’s original color palette & footer copy with the new dynamic classes (`.none`, `.low`, etc.).                                                                |
| **README refresh**        | You’re looking at it.                                                                                                                                                     |

---

## Current status

Prototype **v 0.4** — fully dynamic front‑end.  SMS and automation next.

| Done | Feature                                                    |
| ---- | ---------------------------------------------------------- |
| ✅    | Semantic landing page with date & *last updated* timestamp |
| ✅    | Responsive styling, severity color‑coding                  |
| ✅    | Live pollen data via Tomorrow\.io ‑ fetched client‑side    |
| 🚧   | Twilio SMS engine                                          |
| 🚧   | Scheduled GitHub Action (daily cron)                       |

---

## Roadmap

| Stage                      | Tasks                                                                                    | Target |
| -------------------------- | ---------------------------------------------------------------------------------------- | ------ |
| **MVP – Automated SMS**    | Call Tomorrow\.io daily in a GitHub Action → send SMS via Twilio (store secrets in repo) | v 1.0  |
| **Dashboard – 7‑day view** | Persist the last week’s pollen in JSON → show Recharts line chart; add PWA manifest      | v 1.1  |
| **Polish & Growth**        | Retry logic, multi‑user support, Cypress tests, Plausible analytics                      | v 1.2+ |

---

## Tech stack

- **Frontend:** vanilla HTML / CSS / JS
- **Data:** Tomorrow\.io Timelines API
- **Messaging:** Twilio Programmable SMS
- **Automation:** GitHub Actions daily cron
- **Hosting:** GitHub Pages (Jekyll minimal theme)

---

## Local development

```bash
# Clone & serve
$ git clone https://github.com/gtharp/Jenny-Allergy-App.git
$ cd Jenny-Allergy-App
$ open index.html   # or use Live Server in VS Code
```

### Using your own API key

1. Grab a free Tomorrow\.io key.
2. In `index.html`, replace `YOUR_TOMORROW_IO_API_KEY` with the real key **in quotes**:

```js
const API_KEY = "4EyBh-…";
```

*(The quotes are essential — otherwise JavaScript thinks **``** is scientific notation and VS Code warns “Digit expected.”)*

### When the backend is ready

```bash
pip install -r requirements.txt
export TWILIO_SID=… TWILIO_TOKEN=… POLLEN_API_KEY=…
python src/send_sms.py
```

---

## Contributing

Pull requests welcome! Open an issue first to discuss major changes.

## License

MIT — see `LICENSE` for details.

