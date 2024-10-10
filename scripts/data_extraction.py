import os
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def load_data():
    # Check if we're using Google Sheets or local CSV
    if os.getenv("USE_GOOGLE_SHEETS", "false").lower() == "true":
        return load_from_google_sheets()
    else:
        return load_from_csv()

def load_from_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"), scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(os.getenv("DUMMY_DATA_SPREADSHEET")).sheet1
    data = sheet.get_all_records()
    return pd.DataFrame(data)

def load_from_csv():
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'data.csv')
    return pd.read_csv(csv_path)
