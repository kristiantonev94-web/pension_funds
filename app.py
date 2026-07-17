import streamlit as st
from databricks import sql
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Pension Dashboard",
    page_icon="📈",
    layout="wide"
)


# -----------------------------
# Load data from Databricks
# -----------------------------

@st.cache_data(
    ttl=3600,
    show_spinner=False
)
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
            WHERE Type = 'UPF'
            AND Value > 0
            """,
            connection
        )

    return df



# -----------------------------
# Prepare data
# -----------------------------

df = load_data()


# Date format
df["Date"] = pd.to_datetime(
    df["Date"]
)


# Clean fund names
df["Fund"] = (
    df["Fund"]
    .astype(str)
    .str.replace('"', '', regex=False)
)


# Keep only UPF
df = df[
    df["Type"] == "UPF"
].copy()


# Convert value
df["Value"] = pd.to_numeric(
    df["Value"],
    errors="coerce"
)




# -----------------------------
# Currency conversion
# -----------------------------

euro_date = pd.Timestamp(
    "2026-01-01"
)

df["Price_EUR"] = df["Value"]


# Before euro adoption:
# BGN -> EUR

df.loc[
    df["Date"] < euro_date,
    "Price_EUR"
] = (
    df.loc[
        df["Date"] < euro_date,
        "Value"
    ] / 1.95583
)


# Sort data

df = df.sort_values(
    [
        "Fund",
        "Date"
    ]
)


# -----------------------------
# Dashboard
# -----------------------------

st.title(
    "📈 Bulgarian Pension Funds - UPF Prices"
)


st.write(
    f"Available UPF funds: {df['Fund'].nunique()}"
)


# -----------------------------
# Chart - all funds
# -----------------------------

fig = px.line(
    df,
    x="Date",
    y="Price_EUR",
    color="Fund",
    title="UPF pension fund prices (EUR)",
)


fig.update_layout(
    yaxis_title="Price (€)",
    xaxis_title="Date",
    hovermode="x unified",
    legend_title="Fund",
    
    # Allow clicking legend items
    legend=dict(
        itemclick="toggleothers",
        itemdoubleclick="toggle"
    )
)


st.plotly_chart(
    fig,
    width="stretch"
)



# -----------------------------
# Data preview
# -----------------------------

with st.expander(
    "Show data"
):

    st.dataframe(
        df,
        width="stretch"
    )
