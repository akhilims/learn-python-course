import streamlit as st
from pipeline import load
week = load()
st.title("Fetched and joined")
st.dataframe(week)
