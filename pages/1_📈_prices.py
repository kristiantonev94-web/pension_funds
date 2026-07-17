"""
Prices Dashboard Page
Displays UPF pension fund prices and trends
"""

import streamlit as st
from utils.data_loader import load_prices_data
from utils.data_processor import process_prices_data
from utils.charts import create_prices_line_chart


st.set_page_config(
    page_title="Prices - Pension Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 UPF Pension Fund Prices")

# Load and process data
with st.spinner("Loading prices data..."):
    df = load_prices_data()
    df = process_prices_data(df)

# Display summary
st.metric(
    label="Available UPF Funds",
    value=df['Fund'].nunique()
)

# Create and display chart
fig = create_prices_line_chart(df)
st.plotly_chart(fig, use_container_width=True)

# Data preview
with st.expander("📊 Show price data"):
    st.dataframe(df, use_container_width=True)
    
    # Download option
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download as CSV",
        data=csv,
        file_name="pension_prices.csv",
        mime="text/csv"
    )
