import plotly.express as px
import streamlit as st
from pipeline import load
px.defaults.template = "plotly_white"
week = load()
opts = week.city.unique()
side = st.sidebar
pick = side.multiselect("City", opts, opts)
days = side.slider("Last days", 1, 7, 7)
if not pick:
    st.warning("Pick at least one city")
    st.stop()
view = week[week.city.isin(pick)]
last = sorted(view.date.unique())[-days:]
view = view[view.date.isin(last)]
rank = view.groupby("city").rain_mm.sum()
rank = rank.round(1).sort_values()
top = rank.index[-1]
st.title(f"{top} needs riders first")
st.caption("Rain in mm. Data: Open-Meteo")
st.metric("Rain there", f"{rank[top]} mm")
bars = px.bar(rank, orientation="h")
bars.update_xaxes(title="Rain (mm)")
bars.update_yaxes(title="")
bars.update_layout(showlegend=False)
bars.update_traces(texttemplate="%{x}")
bars.update_traces(textposition="outside")
bars.update_traces(cliponaxis=False)
st.plotly_chart(bars)
csv = view.to_csv(index=False)
st.download_button("Save", csv, "rain.csv")
