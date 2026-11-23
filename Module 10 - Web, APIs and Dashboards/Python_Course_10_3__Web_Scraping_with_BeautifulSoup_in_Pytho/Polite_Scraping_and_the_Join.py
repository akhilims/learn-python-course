# Polite Scraping and the Join
# Every cell of the notebook, in order, as one script (run: python Polite_Scraping_and_the_Join.py)

# Activate the project's Python again

# Reading robots.txt with RobotFileParser

import requests
from urllib.robotparser import RobotFileParser
me = {"User-Agent": "RainReadyDesk/1.0"}
site = "https://en.wikipedia.org"
url = site + "/robots.txt"
txt = requests.get(url, headers=me, timeout=30).text
rp = RobotFileParser()
rp.parse(txt.splitlines())

# can_fetch: is this address allowed?

title = "List_of_cities_in_India_by_population"
ok = site + "/wiki/" + title
no = site + "/w/index.php"
print(rp.can_fetch("RainReadyDesk", ok))
print(rp.can_fetch("RainReadyDesk", no))

# A polite pause with time.sleep

import time
for name in ["Mumbai", "Delhi"]:
    page = site + "/wiki/" + name
    r = requests.get(page, headers=me, timeout=30)
    print(name, r.status_code)
    time.sleep(1)

# Joining rain and population with merge

import pandas as pd
pop = pd.read_csv("population.csv")
cities = ["Mumbai", "Delhi", "Bengaluru", "Chennai", "Kolkata"]
mm = [136.5, 5.4, 0.3, 0.5, 10.0]
rain = pd.DataFrame({"city": cities})
rain["rain_mm"] = mm
both = rain.merge(pop, on="city")
print(both)

# Rain per million people: the fair ranking

both["millions"] = both["people"] / 1000000
both["rate"] = both["rain_mm"] / both["millions"]
both["rate"] = both["rate"].round(2)
print(both.sort_values("rate", ascending=False))
