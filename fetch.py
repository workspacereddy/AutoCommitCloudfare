import json
import requests
from datetime import datetime

URL = "https://database.gformsnap.xyz/read?token=qazwsxedcrfv"

def fetch_and_save():
    try:
        print("Fetching data...")
        response = requests.get(URL, timeout=15)

        response.raise_for_status()  # Throw error if status != 200

        data = response.json()

        # Write JSON file
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        # Log
        with open("fetch_log.txt", "a") as log:
            log.write(f"[{datetime.utcnow().isoformat()}] Data updated\n")

        print("✔ Data saved to data.json")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    fetch_and_save()
