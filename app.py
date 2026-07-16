import streamlit as st
from utils.load_data import load_pension_data


st.set_page_config(
    page_title="Pension Dashboard",
    page_icon="📈",
    layout="wide"
)


st.title("📈 Pension Dashboard")


df = load_pension_data()


st.metric(
    "Total records",
    len(df)
)


st.dataframe(
    df,
    use_container_width=True
)
