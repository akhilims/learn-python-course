# Python Course 10.3 Part 1: Web Scraping with BeautifulSoup
# Every cell of the notebook, in order, as one script (run: python Python_Course_10_3_Part_1__Web_Scraping_with_Beaut.py)

# Create and activate the virtual environment

# Install requests and beautifulsoup4 with pip

# Download and save the web page with requests

import requests
from pathlib import Path
page = "https://en.wikipedia.org/wiki/"
page += "List_of_cities_in_India_by_population"
page += "?oldid=1385294039"
me = {"User-Agent": "RainReadyDesk/1.0"}
r = requests.get(page, headers=me, timeout=30)
r.raise_for_status()
print(r.status_code)
saved = Path("page.html")
saved.write_text(r.text, encoding="utf-8")
print(saved.read_text(encoding="utf-8")[:15])

# Read the HTML with BeautifulSoup: find and find_all

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table", class_="wikitable")
rows = table.find_all("tr")
print(len(rows))

# Find the five delivery cities in the table rows

desk = ["Mumbai", "Delhi", "Bengaluru", "Chennai", "Kolkata"]
for row in rows[2:]:
    cells = row.find_all(["th", "td"])
    name = cells[0].get_text(strip=True)
    if name.startswith(tuple(desk)):
        print(name, cells[2].get_text(strip=True))
