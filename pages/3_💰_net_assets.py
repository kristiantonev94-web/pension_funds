"""
Net Assets Value Dashboard Page
Displays UPF pension fund net assets value trends and analysis
"""

import streamlit as st
from utils.data_loader import load_net_assets_data
from utils.data_processor import process_net_assets_data, calculate_market_share, get_latest_ranking
from utils.charts import create_net_assets_trend_chart, create_net_assets_market_share_chart


st.set_page_config(
    page_title="Net Assets - Pension Dashboard",
    page_icon="💰",
    layout="wide"
)

st.title("💰 UPF Net Assets Value")

# Load and process data
with st.spinner("Loading net assets data..."):
    net_assets = load_net_assets_data()
    net_assets = process_net_assets_data(net_assets)

# Display summary metrics
col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Available UPF Funds",
        value=net_assets['Fund'].nunique()
    )

with col2:
    latest_total = net_assets[
        (net_assets['Year'] == net_assets['Year'].max()) & 
        (net_assets['Month'] == net_assets[net_assets['Year'] == net_assets['Year'].max()]['Month'].max())
    ]['Value'].sum()
    st.metric(
        label="Total Net Assets (Latest)",
        value=f"€{latest_total:,.0f}"
    )

# View selection
view_type = st.radio(
    "Select View:",
    ["Trend", "Market Share"],
    horizontal=True
)

if view_type == "Trend":
    st.subheader("Net Assets Value Trend")
    fig = create_net_assets_trend_chart(net_assets)
    st.plotly_chart(fig, width="stretch")
    
else:
    st.subheader("Market Share Analysis")
    
    # Calculate market share
    market = calculate_market_share(net_assets)
    ranking = get_latest_ranking(market)
    
    # Show latest ranking
    st.caption(
        "**Current Ranking (Latest Month):** " +
        " → ".join(
            [f"{i+1}. {fund}" for i, fund in enumerate(ranking)]
        )
    )
    
    fig = create_net_assets_market_share_chart(market)
    st.plotly_chart(fig, width="stretch")

# Data preview
with st.expander("📊 Show net assets data"):
    st.dataframe(net_assets, width="stretch")
    
    # Download option
    csv = net_assets.to_csv(index=False)
    st.download_button(
        label="Download as CSV",
        data=csv,
        file_name="pension_net_assets.csv",
        mime="text/csv"
    )
