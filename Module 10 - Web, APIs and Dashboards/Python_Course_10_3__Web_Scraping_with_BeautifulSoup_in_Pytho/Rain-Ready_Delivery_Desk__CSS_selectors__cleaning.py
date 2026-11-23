# Rain-Ready Delivery Desk: CSS selectors, cleaning and read_html
# Every cell of the notebook, in order, as one script (run: python Rain-Ready_Delivery_Desk__CSS_selectors__cleaning.py)

# Activate the project's own Python

# Install pandas and lxml for read_html

# CSS selectors with select

from pathlib import Path
from bs4 import BeautifulSoup
html = Path("page.html").read_text(encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")
rows = soup.select("table.wikitable tr")
cells = rows[2].select("th, td")
print([c.get_text(strip=True) for c in cells][:3])

# Cleaning all 340 cities into real numbers

data = []
for row in rows[2:]:
    cells = row.select("th, td")
    name = cells[0].get_text(strip=True)
    name = name.replace(chr(8225), "")
    people = cells[2].get_text(strip=True)
    people = int(people.replace(",", ""))
    data.append({"city": name, "people": people})
print(len(data))
print(data[0])

# Build a DataFrame and save cities.csv

import pandas as pd
cities = pd.DataFrame(data)
cities.to_csv("cities.csv", index=False)
print(cities.head(3))
print(open("cities.csv").read()[:60])

# Filter the five desk cities into population.csv

desk = ["Mumbai", "Delhi", "Bengaluru", "Chennai", "Kolkata"]
pop = cities[cities["city"].isin(desk)]
pop.to_csv("population.csv", index=False)
print(pop)

# The shortcut: pandas read_html

from io import StringIO
tables = pd.read_html(StringIO(html))
print(len(tables))
print(tables[0].shape)
