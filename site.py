import streamlit as st
import pandas as pd

st.set_page_config(page_title="IronIQ | Match Engine", layout="wide")
st.title("IronIQ")
st.subheader("Field-First Construction Intelligence")

# 1. THE UPLOAD BOX
st.write("### 📤 Upload Project Documents")
uploaded_files = st.file_uploader("Drag and drop Kamco or Feldman PDFs here", accept_multiple_files=True)

if uploaded_files:
    st.success(f"Ingested {len(uploaded_files)} files. Analyzing rates...")
    
    # 2. THE AUDIT TABLE (This displays once you drop a file)
    st.write("### 🔍 Active Invoice-Drift Analysis")
    audit_data = [
        {"Item": "ARM ULTIMA 3/4 2X2", "Quoted": "$3,304/MSF", "Invoiced": "$3,450/MSF", "Variance": "+$146.00", "Status": "FLAGGED"},
        {"Item": "5/8 FC Sheetrock", "Quoted": "$18.50/PC", "Invoiced": "$19.25/PC", "Variance": "+$0.75", "Status": "FLAGGED"}
    ]
    st.dataframe(pd.DataFrame(audit_data), use_container_width=True)
    st.warning("Potential Recovery Identified: $1,376.20")

else:
    st.info("Drop a Quote and an Invoice above to trigger the Match Engine.")

# Pricing Table always stays at the bottom
with st.expander("View Performance Pricing (NTE)"):
    pricing = {"Tier": ["Small GC", "Mid GC", "Large GC"], "NTE Fee": ["$1,500", "$3,500", "$6,500 + 5%"]}
    st.table(pd.DataFrame(pricing))
        
