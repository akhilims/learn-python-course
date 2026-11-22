# Rain for Five Cities with requests
# Every cell of the notebook, in order, as one script (run: python Rain_for_Five_Cities_with_requests.py)

# ## The cities file: five delivery cities in one dictionary

# ## Virtual environment and pip install requests

# ## requests.get with params, timeout and raise_for_status

import requests
from cities import cities
api = "https://archive-api.open-meteo.com"
api += "/v1/archive"
lat, lon = cities["Mumbai"]
ask = {"daily": "rain_sum"}
ask["latitude"] = lat
ask["longitude"] = lon
ask["start_date"] = "2025-08-19"
ask["end_date"] = "2025-08-19"
ask["timezone"] = "Asia/Kolkata"
r = requests.get(api, params=ask, timeout=30)
r.raise_for_status()
print(r.status_code)
print(r.headers["Content-Type"])
print(r.json()["daily"])

# ## A wrong date: reading a 400 status and the reason

bad = dict(ask, end_date="2025-13-01")
r = requests.get(api, params=bad, timeout=30)
print(r.status_code)
print(r.json()["reason"])
print(r.json().get("daily"))

# ## json_normalize: rain for five cities in one flat table

import pandas as pd
rows = []
for name, (lat, lon) in cities.items():
    ask["latitude"] = lat
    ask["longitude"] = lon
    r = requests.get(api, params=ask, timeout=30)
    r.raise_for_status()
    one = r.json()
    one["city"] = name
    rows.append(one)
df = pd.json_normalize(rows)
df["rain"] = df["daily.rain_sum"].str[0]
print(df[["city", "rain"]])
