import streamlit as st
from databricks import sql
import pandas as pd


@st.cache_data(ttl=3600)
def load_data():

    with sql.connect(
        server_hostname=st.secrets["databricks"]["server_hostname"],
        http_path=st.secrets["databricks"]["http_path"],
        access_token=st.secrets["databricks"]["access_token"]
    ) as connection:

        df = pd.read_sql(
            """
            SELECT *
            FROM analytics.main.pensions_prices
            """,
            connection
        )

    return df
