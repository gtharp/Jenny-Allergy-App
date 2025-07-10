# Jenny Allergy App

Daily pollen & allergen alerts for Jenny in San Antonio, TX — delivered straight to her phone.

> **Goal:** Each morning (6 AM CDT) Jenny receives a concise SMS telling her whether cedar, ragweed, or mold spores are going to ruin the day.

---

## 🚀 Current Status (Prototype v0.2)

| Done | Feature                                                                                                                                      |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅    | **Semantic landing page** (`index.html`) with a modern card layout, accessible color scheme, and automatic “today” date injection.           |
| ✅    | **Refactored styles** (`styles.css`) using CSS custom properties, mobile‑first sizing, and color‑coded status pills (low / moderate / high). |
| ✅    | **Project scaffolding** – repo cleaned, empty `_config.yml` removed, README created.                                                         |

*There is ****no backend yet****: the status text is still static.*

---

## 🗺️ Roadmap

| Stage                     | Tasks                                                                                                                                                                                                                                                                                                                                                           | Target    |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| **MVP – Automated SMS**   | ⛅ **Pollen data**: Fetch daily forecast from an API (Ambee, Tomorrow\.io, or WeatherKit).📲 **SMS engine**: Use Twilio (or free e‑mail→SMS gateway) to send Jenny the result.⚙️ **Scheduler**: GitHub Action (`.github/workflows/daily_sms.yml`) that runs at 11:00 UTC (06:00 CDT).🔑 **Secrets**: Store API keys & phone numbers in GitHub encrypted secrets. | **v1.0**  |
| **Dashboard – Live site** | 🌡️ Display live pollen count on the landing page via JS fetch.📈 7‑day history chart (Recharts).📱 PWA manifest so Jenny can “install” it.                                                                                                                                                                                                                     | **v1.1**  |
| **Polish & Growth**       | ⏱️ Retry + alert logic when API fails.👥 Multi‑user support via environment list.📊 Plausible analytics.🧪 Cypress tests for API fallback & SMS formatting.                                                                                                                                                                                                     | **v1.2+** |

---

## 🏗️ Tech Stack (planned)

- **Frontend**: vanilla HTML + CSS (no frameworks)
- **Data**: Ambee / Tomorrow\.io pollen API
- **Messaging**: Twilio Programmable SMS
- **Automation**: GitHub Actions on a daily cron
- **Hosting**: GitHub Pages for the static site

---

## 🔧 Local Setup (for now)

```bash
# 1. Clone
$ git clone https://github.com/gtharp/Jenny-Allergy-App.git
$ cd Jenny-Allergy-App

# 2. Open index.html in a browser — that’s it (current prototype is static)
```

When the backend is in place you’ll instead:

```bash
# Install deps & run locally (planned)
$ pip install -r requirements.txt
$ export TWILIO_SID=... TWILIO_TOKEN=... POLLEN_API_KEY=...
$ python src/send_sms.py
```

---

## 📂 File Structure

```
repo/
 ├─ index.html          # Landing page (live pollen view)
 ├─ styles.css          # Theme & layout
 ├─ .github/
 │   └─ workflows/
 │       └─ daily_sms.yml   # Scheduler (todo)
 ├─ src/                # Backend scripts (todo)
 │   └─ send_sms.py
 └─ README.md          # You are here
```

---

## 🙋‍♀️ Contributing / Ideas

This is a personal project, but PRs or issue suggestions are welcome — especially around:

- Free or low‑cost pollen APIs
- Better SMS copywriting (140‑char friendly!)
- Tips for multi‑city expansion

---

## 📜 License

MIT — have fun, but double‑check your allergy meds 😄

