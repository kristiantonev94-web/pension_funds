"""
Insured Persons Dashboard Page
Displays UPF insured persons trends and market share
"""

import streamlit as st
from utils.data_loader import load_members_data
from utils.data_processor import (
    process_members_data,
    calculate_market_share,
    get_latest_ranking,
    order_funds_by_ranking
)
from utils.charts import create_members_trend_chart, create_market_share_chart


st.set_page_config(
    page_title="Members - Pension Dashboard",
    page_icon="👥",
    layout="wide"
)

st.title("👥 UPF Insured Persons")

# Load and process data
with st.spinner("Loading members data..."):
    members = load_members_data()
    members = process_members_data(members)

# Display summary
st.metric(
    label="Available UPF Funds",
    value=members['Fund'].nunique()
)

# View selection
view_type = st.radio(
    "Select View:",
    ["Trend", "Market Share"],
    horizontal=True
)

if view_type == "Trend":
    st.subheader("Insured Persons Trend")
    fig = create_members_trend_chart(members)
    st.plotly_chart(fig, use_container_width=True)
    
else:
    st.subheader("Market Share Analysis")
    
    # Calculate market share
    market = calculate_market_share(members)
    ranking = get_latest_ranking(market)
    market = order_funds_by_ranking(market, ranking)
    
    # Show latest ranking
    st.caption(
        "**Current Ranking (Latest Month):** " +
        " → ".join(
            [f"{i+1}. {fund}" for i, fund in enumerate(ranking)]
        )
    )
    
    fig = create_market_share_chart(market)
    st.plotly_chart(fig, use_container_width=True)

# Data preview
with st.expander("📊 Show insured persons data"):
    st.dataframe(members, use_container_width=True)
    
    # Download option
    csv = members.to_csv(index=False)
    st.download_button(
        label="Download as CSV",
        data=csv,
        file_name="pension_members.csv",
        mime="text/csv"
    )
