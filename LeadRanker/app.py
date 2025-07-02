import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="LeadRanker", layout="centered")

st.title("📊 LeadRanker - Scored Lead Viewer")

# Check if the file exists
file_path = "data/scored_leads.csv"

if not os.path.exists(file_path):
    st.error("❌ File not found: data/scored_leads.csv")
    st.stop()

# Load the scored leads
df = pd.read_csv(file_path)

# Sidebar filter
st.sidebar.header("🔍 Filter Leads")
confidence_filter = st.sidebar.multiselect(
    "Select Confidence Level",
    options=df["confidence_label"].unique(),
    default=df["confidence_label"].unique()
)

# Apply filter
filtered_df = df[df["confidence_label"].isin(confidence_filter)]

# Display data
st.subheader("📄 Filtered Leads")
st.dataframe(filtered_df, use_container_width=True)

# Download button
def convert_df(df):
    return df.to_csv(index=False).encode("utf-8")

csv_data = convert_df(filtered_df)
st.download_button(
    label="📥 Download Filtered Leads as CSV",
    data=csv_data,
    file_name="filtered_leads.csv",
    mime="text/csv"
)

# Footer
st.markdown("---")
st.caption("🚀 Built by Ayushman for Caprae Capital's AI-Readiness Challenge")
