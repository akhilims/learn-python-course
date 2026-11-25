import pandas as pd
import requests
import streamlit as st
api = "https://archive-api.open-meteo.com"
api += "/v1/archive"
ask = {"daily": "rain_sum"}
ask["timezone"] = "Asia/Kolkata"
ask["start_date"] = "2025-08-13"
ask["end_date"] = "2025-08-19"
new = {"time": "date", "rain_sum": "rain_mm"}
@st.cache_data
def load():
    cities = pd.read_csv("desk_cities.csv")
    rows = []
    for c in cities.itertuples():
        q = dict(ask, latitude=c.lat)
        q["longitude"] = c.lon
        r = requests.get(api, params=q)
        day = pd.DataFrame(r.json()["daily"])
        day["city"] = c.city
        rows.append(day)
    week = pd.concat(rows)
    week = week.rename(columns=new)
    return week.merge(cities)
