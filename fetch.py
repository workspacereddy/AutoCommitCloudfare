import json
import requests
from datetime import datetime

URL = "https://database.gformsnap.xyz/read?token=qazwsxedcrfv"

response = requests.get(URL, timeout=15)
data = response.json()

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("fetch_log.txt", "a") as log:
    log.write(f"[{datetime.utcnow().isoformat()}] Auto update\n")
