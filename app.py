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
# Load prices data from Databricks
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
# Load insured persons data
# -----------------------------

@st.cache_data(
    ttl=3600,
    show_spinner=False
)
def load_members():

    with sql.connect(
        server_hostname=st.secrets["databricks"]["server_hostname"],
        http_path=st.secrets["databricks"]["http_path"],
        access_token=st.secrets["databricks"]["access_token"]
    ) as connection:

        df = pd.read_sql(
            """
            SELECT *
            FROM analytics.main.pension_fund_members_upf
            """,
            connection
        )

    return df


# -----------------------------
# Prepare price data
# -----------------------------

df = load_data()

df["Value"] = pd.to_numeric(
    df["Value"],
    errors="coerce"
)

df = df.sort_values(
    [
        "Fund",
        "Date"
    ]
)


# -----------------------------
# Prepare insured persons data
# -----------------------------

members = load_members()

members["Value"] = pd.to_numeric(
    members["Value"],
    errors="coerce"
)

members["Date"] = pd.to_datetime(
    dict(
        year=members["Year"],
        month=members["Month"],
        day=1
    )
)

members = members.sort_values(
    [
        "Fund",
        "Date"
    ]
)


# -----------------------------
# Dashboard
# -----------------------------

st.title(
    "📈 Bulgarian Pension Funds - UPF"
)


st.write(
    f"Available UPF funds: {df['Fund'].nunique()}"
)


# -----------------------------
# Chart - fund prices
# -----------------------------

fig = px.line(
    df,
    x="Date",
    y="Value",
    color="Fund",
    title="UPF pension fund prices (EUR)",
)


fig.update_layout(
    yaxis_title="Price (€)",
    xaxis_title="Date",
    hovermode="x unified",
    legend_title="Fund",

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
# Price data preview
# -----------------------------

with st.expander(
    "Show price data"
):

    st.dataframe(
        df,
        width="stretch"
    )


# -----------------------------
# Chart - insured persons
# -----------------------------

st.subheader(
    "👥 UPF insured persons"
)


fig_members = px.line(
    members,
    x="Date",
    y="Value",
    color="Fund",
    title="Number of insured persons in UPF",
)


fig_members.update_layout(
    yaxis_title="Insured persons",
    xaxis_title="Date",
    hovermode="x unified",
    legend_title="Fund",

    legend=dict(
        itemclick="toggleothers",
        itemdoubleclick="toggle"
    )
)


st.plotly_chart(
    fig_members,
    width="stretch"
)


# -----------------------------
# Members data preview
# -----------------------------

with st.expander(
    "Show insured persons data"
):

    st.dataframe(
        members,
        width="stretch"
    )
