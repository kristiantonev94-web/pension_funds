"""
Data loading module for Pension Funds Dashboard
Handles all database connections and data fetching
"""

import streamlit as st
import pandas as pd
from databricks import sql
from config import get_databricks_connection_params, PRICES_TABLE, MEMBERS_TABLE, NET_ASSETS_TABLE, PRICE_TYPE_FILTER, PRICE_VALUE_MIN, CACHE_TTL


@st.cache_data(
    ttl=CACHE_TTL,
    show_spinner=False
)
def load_prices_data():
    """Load pension fund prices from Databricks"""
    
    connection_params = get_databricks_connection_params()
    
    with sql.connect(**connection_params) as connection:
        df = pd.read_sql(
            f"""
            SELECT *
            FROM {PRICES_TABLE}
            WHERE Type = '{PRICE_TYPE_FILTER}'
            AND Value > {PRICE_VALUE_MIN}
            """,
            connection
        )
    
    return df


@st.cache_data(
    ttl=CACHE_TTL,
    show_spinner=False
)
def load_members_data():
    """Load insured persons data from Databricks"""
    
    connection_params = get_databricks_connection_params()
    
    with sql.connect(**connection_params) as connection:
        df = pd.read_sql(
            f"""
            SELECT *
            FROM {MEMBERS_TABLE}
            """,
            connection
        )
    
    return df


@st.cache_data(
    ttl=CACHE_TTL,
    show_spinner=False
)
def load_net_assets_data():
    """Load net assets value data from Databricks"""
    
    connection_params = get_databricks_connection_params()
    
    with sql.connect(**connection_params) as connection:
        df = pd.read_sql(
            f"""
            SELECT *
            FROM {NET_ASSETS_TABLE}
            """,
            connection
        )
    
    return df
