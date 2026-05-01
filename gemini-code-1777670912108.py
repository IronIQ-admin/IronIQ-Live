import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(page_title="IronIQ | Invoice-Drift Intelligence", layout="wide")

# Header
st.title("IronIQ")
st.subheader("Field-First Construction Intelligence")

# 1. Performance-Based Pricing Table (NTE Model)
st.write("### Performance-Based Pricing (NTE)")
pricing_data = {
    "Tier": ["Small GC", "Mid-Size GC", "Large GC"],
    "Revenue Range": ["Under $10M", "$10M – $50M", "Over $50M"],
    "Monthly NTE Fee": ["$1,500", "$3,500", "$6,500 + 5%"],
    "Activation Trigger": ["Savings reach $1,500", "Savings reach $3,500", "Base + 5% of recovery"]
}
st.table(pd.DataFrame(pricing_data))

# 2. Automated Audit Results
st.write("### Active Invoice-Drift Analysis (Job #2356)")

st.success("Kamco Documents Ingested. Discrepancies identified.")

# Raw Data extracted from your Kamco uploads
drift_results = [
    {"Item": "ARM ULTIMA 3/4\" 2X2", "Quoted Rate": "$3,304.00/MSF", "Invoiced Rate": "$3,450.00/MSF", "Drift": "$146.00", "Status": "FLAGGED"},
    {"Item": "ARM 9/16\" 12' SILHOUETTE", "Quoted Rate": "$2,006.00/MLF", "Invoiced Rate": "$2,100.00/MLF", "Drift": "$94.00", "Status": "FLAGGED"},
    {"Item": "5/8 FC Sheetrock", "Quoted Rate": "$18.50/PC", "Invoiced Rate": "$19.25/PC", "Drift": "$0.75", "Status": "FLAGGED"}
]
st.dataframe(pd.DataFrame(drift_results), use_container_width=True)

st.warning("Total Identified Drift for Job 2356: $1,376.20")
st.info("Siloed Environment | Built for the Field by a 20-Year Superintendent")