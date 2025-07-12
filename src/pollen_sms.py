"""
Fetch San Antonio pollen indices from Tomorrow.io and send an SMS.
"""

from datetime import date
import os
import requests
from twilio.rest import Client

# --- Config ---------------------------------------------------------------
LAT, LON = 29.4241, -98.4936  # San Antonio, TX
API_KEY      = os.environ["POLLEN_API_KEY"]      # Tomorrow.io key (secret)
TWILIO_SID   = os.environ["TWILIO_SID"]          # Twilio creds (secret)
TWILIO_TOKEN = os.environ["TWILIO_TOKEN"]
TWILIO_FROM  = os.environ["TWILIO_FROM"]         # Your Twilio number  e.g. +12345550123
TO_NUMBER    = os.environ["JENNY_PHONE"]         # Jenny’s phone        e.g. +12105550123
# --------------------------------------------------------------------------

def fetch_pollen():
    """Return dict with tree and ragweed index values (0–5) for today."""
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

LEVEL = ["None", "Very Low", "Low", "Moderate", "High", "Very High"]

def make_message(vals: dict) -> str:
    today = date.today().strftime("%a %m/%d")
    cedar = LEVEL[vals["treeIndex"]]
    rag   = LEVEL[vals["weedRagweedIndex"]]
    return f"{today} pollen ➜ Cedar: {cedar} / Ragweed: {rag}"

def send_sms(body: str):
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    client.messages.create(to=TO_NUMBER, from_=TWILIO_FROM, body=body)

if __name__ == "__main__":
    vals = fetch_pollen()
    msg  = make_message(vals)
    send_sms(msg)
    print("SMS sent:", msg)
