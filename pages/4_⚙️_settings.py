"""
Settings Page
Application configuration and information
"""

import streamlit as st

st.set_page_config(
    page_title="Settings - Pension Dashboard",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Settings")

st.markdown("---")

st.subheader("📋 About This Dashboard")
st.write(
    """
    This dashboard provides comprehensive insights into Bulgarian UPF (Unit-Linked Fund) pension funds.
    
    **Features:**
    - Real-time fund prices in EUR
    - Insured persons trends
    - Market share analysis
    - Historical data visualization
    
    **Data Source:** Databricks Analytics Warehouse
    
    **Last Updated:** Data refreshes hourly
    """
)

st.markdown("---")

st.subheader("🔧 Technical Details")
st.write(
    """
    - Built with Streamlit
    - Visualizations by Plotly
    - Data warehouse: Databricks SQL
    - Cache TTL: 1 hour
    """
)

st.markdown("---")

st.subheader("📞 Support")
st.write(
    "For issues or feature requests, please contact the development team."
)
