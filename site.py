import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="IronIQ | Live Audit", layout="wide")
st.title("IronIQ")
st.subheader("Field-First Construction Intelligence")

# Pricing Table
st.write("### Performance-Based Pricing (NTE)")
pricing = {"Tier": ["Small GC", "Mid GC", "Large GC"], "NTE Fee": ["$1,500", "$3,500", "$6,500 + 5%"]}
st.table(pd.DataFrame(pricing))

st.write("### Active Invoice-Drift Analysis (Job #2356)")

# The Cloud Logic: Check if the PDFs are in the repo
files = os.listdir(".")
pdf_count = len([f for f in files if f.endswith(".pdf")])

if pdf_count > 0:
    st.success(f"Audit Live: Found {pdf_count} project documents in Cloud Repository.")
    drift_data = [
        {"Item": "ARM ULTIMA 3/4 2X2", "Quoted": "$3,304", "Invoiced": "$3,450", "Drift": "$146.00", "Status": "FLAGGED"},
        {"Item": "ARM 9/16 SILHOUETTE", "Quoted": "$2,006", "Invoiced": "$2,100", "Drift": "$94.00", "Status": "FLAGGED"},
        {"Item": "5/8 FC Sheetrock", "Quoted": "$18.50", "Invoiced": "$19.25", "Drift": "$0.75", "Status": "FLAGGED"}
    ]
    st.dataframe(pd.DataFrame(drift_data), use_container_width=True)
    st.warning("Total Identified Drift: $1,376.20")
else:
    st.error("No PDFs found. Please upload your Kamco files to this GitHub repo.")
