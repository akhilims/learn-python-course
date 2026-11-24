import pandas as pd
import plotly.express as px
import streamlit as st
px.defaults.template = "plotly_white"
px.defaults.color_continuous_scale = "Blues"
names = {"rain_mm": "Rain (mm)", "color": "Rain (mm)", "total": "Rain so far (mm)"}
st.set_page_config(layout="wide")
week = pd.read_csv("city_rain_week.csv")
people = pd.read_csv("city_rain.csv").set_index("city")
today = week[week["date"] == "2025-08-19"]
top = today.nlargest(1, "rain_mm").iloc[0]
usual = week[week["city"] == top.city].rain_mm.mean()
st.title(f"{top.city} is the wettest today")
st.caption("Rain in mm, 13-19 Aug 2025. Open-Meteo")
a, b, c = st.columns(3)
a.metric("Wettest today", top.city, f"{top.rain_mm} mm")
b.metric("Usual day there", f"{usual:.1f} mm", f"{top.rain_mm - usual:+.1f} mm")
c.metric("People there", f"{people.people[top.city]:,}")
grid = week.pivot(index="city", columns="date", values="rain_mm")
heat = px.imshow(grid, labels=names, title="Rain per day (mm)")
box = px.box(week, x="city", y="rain_mm",
             labels=names, title="Usual range per city")
merged = today.merge(people.reset_index())
tree = px.treemap(merged, path=["city"], values="people",
                  color="rain_mm", labels=names,
                  title="People and rain today")
tree.update_traces(textposition="top right",
    hovertemplate="%{label}<br>%{value:,} people<br>%{color} mm today")
cum = week.assign(total=week.groupby("city").rain_mm.cumsum())
area = px.area(cum, x="date", y="total", color="city",
               labels=names, title="Rain building up")
left, right = st.columns(2)
left.plotly_chart(heat)
right.plotly_chart(box)
left.plotly_chart(tree)
right.plotly_chart(area)
