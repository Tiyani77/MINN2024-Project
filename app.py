import streamlit as st
import pandas as pd

st.title("Mining Health and Safety Dashboard")
st.write("Welcome to my MINN2024 project app!")

workers = pd.read_csv("workers.csv")
equipment = pd.read_csv("equipment.csv")
incidents = pd.read_csv("incidents.csv")

st.subheader("Workers Data")
st.dataframe(workers)

st.subheader("Equipment Data")
st.dataframe(equipment)

st.subheader("Incidents Data")
st.dataframe(incidents)
