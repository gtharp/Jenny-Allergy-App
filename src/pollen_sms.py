"""
Fetch San Antonio pollen indices from Tomorrow.io and email Jenny the results.
"""

from datetime import date
import os
import smtplib
from email.message import EmailMessage

import requests

# --- Config ---------------------------------------------------------------
LAT, LON = 29.4241, -98.4936  # San Antonio, TX
API_KEY            = os.environ["POLLEN_API_KEY"]        # Tomorrow.io key (secret)
EMAIL_ADDRESS      = os.environ["EMAIL_ADDRESS"]          # Sending Gmail account (secret)
EMAIL_APP_PASSWORD = os.environ["EMAIL_APP_PASSWORD"]     # Gmail app password  (secret)
JENNY_EMAIL        = os.environ["JENNY_EMAIL"]            # Jenny's email address (secret)
# --------------------------------------------------------------------------

LEVEL = ["None", "Very Low", "Low", "Moderate", "High", "Very High"]

def fetch_pollen():
    """Return dict with tree and ragweed index values (0-5) for today."""
    url = "https://api.tomorrow.io/v4/timelines"
    params = {
        "location" : f"{LAT},{LON}",
        "fields"   : ["treeIndex", "weedRagweedIndex"],
        "timesteps": "1d",
        "units"    : "imperial",
        "apikey"   : API_KEY,
    }
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()["data"]["timelines"][0]["intervals"][0]["values"]

def make_message(vals: dict) -> tuple[str, str]:
    today = date.today().strftime("%a %m/%d")
    cedar = LEVEL[vals["treeIndex"]]
    rag   = LEVEL[vals["weedRagweedIndex"]]
    subject = f"Pollen report for {today}"
    body = f"Cedar: {cedar}\nRagweed: {rag}\n\nHave a great day!"
    return subject, body

def send_email(subject: str, body: str):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = JENNY_EMAIL
    msg.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    vals = fetch_pollen()
    subject, body = make_message(vals)
    send_email(subject, body)
    print("Email sent:", subject)
