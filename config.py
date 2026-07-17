"""
Configuration module for Pension Funds Dashboard
Handles secrets and application-wide constants
"""

import streamlit as st


def get_databricks_connection_params():
    """Get Databricks connection parameters from secrets"""
    return {
        "server_hostname": st.secrets["databricks"]["server_hostname"],
        "http_path": st.secrets["databricks"]["http_path"],
        "access_token": st.secrets["databricks"]["access_token"]
    }


# Cache TTL
CACHE_TTL = 3600  # 1 hour

# Database configuration
DB_SCHEMA = "analytics.main"
PRICES_TABLE = f"{DB_SCHEMA}.pensions_prices"
MEMBERS_TABLE = f"{DB_SCHEMA}.pension_fund_members_upf"

# Data filters
PRICE_TYPE_FILTER = "UPF"
PRICE_VALUE_MIN = 0
