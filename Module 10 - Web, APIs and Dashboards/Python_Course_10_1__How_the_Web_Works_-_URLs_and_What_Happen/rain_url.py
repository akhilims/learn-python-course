from urllib.parse import urlencode
site = "archive-api.open-meteo.com"
base = "https://" + site + "/v1/archive"
ask = {"latitude": 19.07}
ask["longitude"] = 72.88
ask["start_date"] = "2025-08-19"
ask["end_date"] = "2025-08-19"
ask["hourly"] = "rain,temperature_2m"
ask["timezone"] = "Asia/Kolkata"
print(base + "?" + urlencode(ask))
