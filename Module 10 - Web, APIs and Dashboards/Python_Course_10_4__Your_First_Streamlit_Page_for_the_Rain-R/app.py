import pandas as pd
import streamlit as st
st.title("Rain-Ready Delivery Desk")
pop = pd.read_csv("city_rain.csv")
pick = st.sidebar.selectbox("City", pop["city"])
row = pop[pop["city"] == pick].iloc[0]
avg = pop["rain_mm"].mean()
a, b = st.columns(2)
gap = round(row.rain_mm - avg, 1)
a.metric("Rain mm", row.rain_mm, gap)
b.metric("People", f"{row.people:,}")
st.bar_chart(pop, x="city", y="rain_mm")
