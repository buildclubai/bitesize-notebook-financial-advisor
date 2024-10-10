import os
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def load_data():
    # Decide which method to use based on environment variables or other criteria
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
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Go up one level to the project root directory
    project_root = os.path.dirname(current_dir)

    # Construct the path to the data.csv file
    csv_path = os.path.join(project_root, 'data', 'data.csv')

    # Check if the file exists
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"The file {csv_path} does not exist.")

    # Read the CSV file
    return pd.read_csv(csv_path)
