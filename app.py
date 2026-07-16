import streamlit as st
from databricks import sql
import pandas as pd
import plotly.express as px


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
            """,
            connection
        )

    return df



# Load data
df = load_data()


# Convert dates
df["Date"] = pd.to_datetime(df["Date"])


# Only UPF
df = df[
    df["Type"] == "UPF"
].copy()


# Convert value to numeric
df["Value"] = pd.to_numeric(
    df["Value"],
    errors="coerce"
)


# Currency conversion
conversion_date = pd.Timestamp("2026-01-01")

df["Value_EUR"] = df["Value"]

df.loc[
    df["Date"] < conversion_date,
    "Value_EUR"
] = (
    df.loc[
        df["Date"] < conversion_date,
        "Value"
    ] / 1.95583
)


# Title
st.title("📈 Bulgarian Pension Funds - UPF Price")


# Fund selector
funds = sorted(
    df["Fund"].unique()
)

selected_fund = st.selectbox(
    "Select Fund",
    funds
)


plot_df = df[
    df["Fund"] == selected_fund
].sort_values(
    "Date"
)


# Chart
fig = px.line(
    plot_df,
    x="Date",
    y="Value_EUR",
    title=f"{selected_fund} - UPF price (EUR)"
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


# Show data
with st.expander("Show data"):
    st.dataframe(
        plot_df,
        use_container_width=True
    )
