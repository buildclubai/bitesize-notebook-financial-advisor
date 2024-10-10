import os
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def load_data():
    # Check if we're using Google Sheets or local CSV
    if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
        return load_from_google_sheets()
    else:
        return load_from_csv()

def load_from_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"), scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1kuDZOyzT54yovmmF0pdWypIMPQQF6ZiX8VJGMecVyqI/edit?usp=sharing").sheet1
    data = sheet.get_all_records()
    return pd.DataFrame(data)

def load_from_csv():
    return pd.read_csv("data.csv")
