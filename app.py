"""
Main entry point for Pension Funds Dashboard
Multi-page Streamlit application
"""

import streamlit as st

# Configure the main page
st.set_page_config(
    page_title="Pension Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling for dark mode consistency
st.markdown(
    """
    <style>
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #0e1117;
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: #ffffff;
    }
    
    /* Main content area */
    [data-testid="stMainBlockContainer"] {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* Text colors */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
    }
    
    p, span, div {
        color: #e0e0e0;
    }
    
    /* Links */
    a {
        color: #58a6ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("📈 Pension Dashboard")
st.sidebar.markdown("---")
st.sidebar.write(
    """
    Navigate through different sections using the menu on the left.
    
    Each page provides different insights into Bulgarian UPF pension funds.
    """
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "**Quick Links:**\n"
    "- [Prices](./1_📈_prices)\n"
    "- [Members](./2_👥_members)\n"
    "- [Analytics](./3_📊_analytics)\n"
    "- [Settings](./4_⚙️_settings)"
)

# Main page content
st.title("📈 Bulgarian Pension Funds Dashboard")

st.markdown(
    """
    Welcome to the comprehensive UPF Pension Funds Dashboard!
    
    ### 📊 What's Available?
    
    **1. 📈 Prices Dashboard**
    - Real-time UPF pension fund prices
    - Historical price trends
    - Fund comparison over time
    
    **2. 👥 Members Dashboard**
    - Track insured persons by fund
    - Monitor membership trends
    - Analyze market share distribution
    
    **3. 📊 Analytics & Insights**
    - Advanced analysis and metrics
    - Fund performance comparison
    - Growth analysis
    
    **4. ⚙️ Settings**
    - Application information
    - Technical details
    - Support resources
    
    ### 🚀 Getting Started
    
    Select a page from the menu on the left to begin exploring!
    """
)

st.info(
    "💡 **Tip:** Data is automatically refreshed every hour. "
    "You can download any data table as CSV using the download button in each section."
)
