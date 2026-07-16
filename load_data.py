import streamlit as st
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import io


@st.cache_data(ttl=3600)
def load_pension_data():

    # Create Google credentials from Streamlit secrets
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"]
    )

    # Build Drive service
    drive = build(
        "drive",
        "v3",
        credentials=credentials
    )


    # -----------------------------
    # Find Pensions folder
    # -----------------------------

    pensions = drive.files().list(
        q="name='pensions' and mimeType='application/vnd.google-apps.folder'",
        fields="files(id,name)"
    ).execute()

    pensions_id = pensions["files"][0]["id"]


    # -----------------------------
    # Find Prices folder
    # -----------------------------

    prices = drive.files().list(
        q=f"""
        name='prices'
        and '{pensions_id}' in parents
        and mimeType='application/vnd.google-apps.folder'
        """,
        fields="files(id,name)"
    ).execute()

    prices_id = prices["files"][0]["id"]


    # -----------------------------
    # Get CSV files
    # -----------------------------

    files = drive.files().list(
        q=f"""
        '{prices_id}' in parents
        and mimeType='text/csv'
        """,
        fields="files(id,name)"
    ).execute()


    csv_files = files.get("files", [])

    st.write(
        "CSV files found:",
        len(csv_files)
    )


    # -----------------------------
    # Load CSV files
    # -----------------------------

    all_data = []


    for f in csv_files:

        content = drive.files().get_media(
            fileId=f["id"]
        ).execute()


        df = pd.read_csv(
            io.BytesIO(content)
        )


        df["Source_File"] = f["name"]

        all_data.append(df)


    # Combine
    final_df = pd.concat(
        all_data,
        ignore_index=True
    )


    return final_df
