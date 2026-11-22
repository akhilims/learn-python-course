# Python Course 10.1 Part 3: A Real Download and Nested JSON
# Every cell of the notebook, in order, as one script (run: python Python_Course_10_1_Part_3__A_Real_Download_and_Nes.py)

# ## Download the Mumbai rain with urlopen and save mumbai.json

from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
from rain_url import base, ask
url = base + "?" + urlencode(ask)
with urlopen(url, timeout=30) as resp:
    body = resp.read()
    kind = resp.headers["Content-Type"]
    print(resp.status, kind)
Path("mumbai.json").write_bytes(body)
print("saved mumbai.json")

# ## Load nested JSON into Python with json.loads

import json
f = Path("mumbai.json")
data = json.loads(f.read_text("utf-8"))
print(type(data))
print(list(data))

# ## Walk nested JSON to find the rainiest hour

hourly = data["hourly"]
print(list(hourly))
rain = hourly["rain"]
print(len(rain), max(rain))
top = rain.index(max(rain))
print(hourly["time"][top])
