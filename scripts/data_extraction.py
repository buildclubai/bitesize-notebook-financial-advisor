# This file is part of bitesize-notebook-financial-advisor.
#
# AI Financial Advisor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AI Financial Advisor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AI Financial Advisor. If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (C) 2024 Vincent Koc (https://github.com/vincentkoc)
# Copyright (C) 2024 Hung Nguyen (https://github.com/hung-ngm)

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
