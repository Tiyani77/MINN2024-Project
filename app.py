import streamlit as st
import pandas as pd

st.title("Mining Health and Safety Dashboard")
st.write("Welcome to my MINN2024 project app!")

# Load datasets
workers = pd.read_csv("workers.csv")
equipment = pd.read_csv("equipment.csv")
incidents = pd.read_csv("incidents.csv")

# Display data
st.subheader("Workers Data")
st.dataframe(workers)

st.subheader("Equipment Data")
st.dataframe(equipment)

st.subheader("Incidents Data")
st.dataframe(incidents)


st.header("Risk Analysis & Alerts")

# Worker fatigue alerts
high_fatigue = workers[workers["Fatigue_Level"] == "High"]
if not high_fatigue.empty:
    st.warning("⚠️ Workers with HIGH fatigue detected:")
    st.dataframe(high_fatigue)

# Equipment condition alerts
critical_equipment = equipment[equipment["Condition"] == "Critical"]
if not critical_equipment.empty:
    st.error("🚨 Critical equipment condition detected:")
    st.dataframe(critical_equipment)

# Incident severity alerts
critical_incidents = incidents[incidents["Severity"] == "Critical"]
if not critical_incidents.empty:
    st.error("🚨 Critical incidents recorded:")
    st.dataframe(critical_incidents)


st.header("Visual Insights")

# Incidents per department
st.subheader("Incidents per Department")
incidents_chart = incidents["Department"].value_counts()
st.bar_chart(incidents_chart)

# PPE compliance
st.subheader("PPE Compliance Overview")
ppe_chart = workers["PPE_Compliance"].value_counts()
st.bar_chart(ppe_chart)

# Equipment condition
st.subheader("Equipment Condition Status")
condition_chart = equipment["Condition"].value_counts()
st.bar_chart(condition_chart)
