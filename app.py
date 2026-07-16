import streamlit as st
from databricks import sql
import pandas as pd


st.set_page_config(
    page_title="Pension Dashboard",
    layout="wide"
)


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
            LIMIT 100
            """,
            connection
        )

    return df


st.title("📈 Pension Dashboard")

st.write("Loading data...")


try:
    df = load_data()

    st.success(
        f"Loaded {len(df)} rows"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

except Exception as e:
    st.error("Error connecting to Databricks:")
    st.exception(e)
