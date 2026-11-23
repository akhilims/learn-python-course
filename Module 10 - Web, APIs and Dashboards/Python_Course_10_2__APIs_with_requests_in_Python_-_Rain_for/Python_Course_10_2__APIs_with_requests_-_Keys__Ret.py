# Python Course 10.2: APIs with requests - Keys, Retries, Cache and Checks in Python (Part 2 of 2)
# Every cell of the notebook, in order, as one script (run: python Python_Course_10_2__APIs_with_requests_-_Keys__Ret.py)

# ## API keys in environment variables with os.environ

# ## Retries with back-off: a requests Session

import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
busy = [429, 500, 502, 503]
rule = dict(total=3, backoff_factor=1)
retry = Retry(**rule, status_forcelist=busy)
door = HTTPAdapter(max_retries=retry)
s = requests.Session()
s.mount("https://", door)
print(retry.total, retry.status_forcelist)

# ## Caching each week in a JSON file

import json
from pathlib import Path
api = "https://archive-api.open-meteo.com"
api += "/v1/archive"
def week(start, end):
    f = Path(f"rain_{start}.json")
    if f.exists():
        print("from the file", f.name)
        return json.loads(f.read_text())
    ask = {"daily": "rain_sum"}
    ask["latitude"] = 19.07
    ask["longitude"] = 72.88
    ask["timezone"] = "Asia/Kolkata"
    ask["start_date"] = start
    ask["end_date"] = end
    r = s.get(api, params=ask, timeout=30)
    r.raise_for_status()
    f.write_text(r.text)
    print("from the server", r.status_code)
    return r.json()

# ## Pagination: August 2025 asked week by week

rain = []
for d in [1, 8, 15, 22, 29]:
    a = f"2025-08-{d:02d}"
    b = f"2025-08-{min(d + 6, 31):02d}"
    page = week(a, b)
    rain += page["daily"]["rain_sum"]
print(len(rain), round(sum(rain), 1))

# ## Reading a cached week without a request

again = week("2025-08-15", "2025-08-21")
print(again["daily"]["rain_sum"][4])

# ## Installing pydantic in the venv

# ## Checking the JSON with a pydantic model

from pydantic import BaseModel, ValidationError
class Daily(BaseModel):
    time: list[str]
    rain_sum: list[float]
ok = Daily(**page["daily"])
print(ok.time[0], ok.rain_sum[0])
bad = {"time": ["2025-08-19"], "rain_sum": ["heavy"]}
try:
    Daily(**bad)
except ValidationError as e:
    print(e.error_count(), e.errors()[0]["msg"])
