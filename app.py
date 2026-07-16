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


# Remove zeros and missing prices
df = df[
    (df["Value"] > 0) &
    (df["Value"].notna())
]


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


# Fund selector

funds = sorted(
    df["Fund"].unique()
)


selected_fund = st.selectbox(
    "Select pension fund",
    funds
)


# Filter selected fund

plot_df = df[
    df["Fund"] == selected_fund
].copy()


# -----------------------------
# Chart
# -----------------------------

fig = px.line(
    plot_df,
    x="Date",
    y="Price_EUR",
    title=f"{selected_fund} - UPF price (EUR)",
)


fig.update_layout(
    yaxis_title="Price (€)",
    xaxis_title="Date",
    hovermode="x unified"
)


st.plotly_chart(
    fig,
    use_container_width=True
)



# -----------------------------
# Data preview
# -----------------------------

with st.expander(
    "Show data"
):

    st.dataframe(
        plot_df,
        use_container_width=True
    )
