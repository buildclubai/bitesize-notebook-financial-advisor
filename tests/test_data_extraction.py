import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import pytest
from scripts.data_extraction import load_data, load_from_csv, load_from_google_sheets

def test_load_data_csv(mocker):
    mocker.patch('os.getenv', return_value='false')
    mock_df = pd.DataFrame({'Date': ['2023-01-01'], 'Description': ['Test'], 'Category': ['Test'], 'Income/Expense': ['Income'], 'Amount': [100]})
    mocker.patch('scripts.data_extraction.load_from_csv', return_value=mock_df)
    result = load_data()
    assert isinstance(result, pd.DataFrame)
    assert 'Date' in result.columns
    assert 'Description' in result.columns
    assert 'Category' in result.columns
    assert 'Income/Expense' in result.columns
    assert 'Amount' in result.columns

def test_load_data_google_sheets(mocker):
    mocker.patch('os.getenv', side_effect=['true', 'dummy_credentials', 'dummy_url'])
    mock_df = pd.DataFrame({'Date': ['2023-01-01'], 'Description': ['Test'], 'Category': ['Test'], 'Income/Expense': ['Income'], 'Amount': [100]})
    mocker.patch('scripts.data_extraction.load_from_google_sheets', return_value=mock_df)
    result = load_data()
    assert isinstance(result, pd.DataFrame)
    assert 'Date' in result.columns
    assert 'Description' in result.columns
    assert 'Category' in result.columns
    assert 'Income/Expense' in result.columns
    assert 'Amount' in result.columns

def test_load_from_csv(mocker):
    mock_df = pd.DataFrame({'Date': ['2023-01-01'], 'Description': ['Test'], 'Category': ['Test'], 'Income/Expense': ['Income'], 'Amount': [100]})
    mocker.patch('pandas.read_csv', return_value=mock_df)
    mocker.patch('os.path.exists', return_value=True)
    result = load_from_csv()
    assert isinstance(result, pd.DataFrame)
    assert 'Date' in result.columns
    assert 'Description' in result.columns
    assert 'Category' in result.columns
    assert 'Income/Expense' in result.columns
    assert 'Amount' in result.columns

def test_load_from_google_sheets(mocker):
    mock_df = pd.DataFrame({'Date': ['2023-01-01'], 'Description': ['Test'], 'Category': ['Test'], 'Income/Expense': ['Income'], 'Amount': [100]})
    mock_client = mocker.Mock()
    mock_sheet = mocker.Mock()
    mock_sheet.get_all_records.return_value = mock_df.to_dict('records')
    mock_client.open_by_url.return_value.sheet1 = mock_sheet
    mocker.patch('gspread.authorize', return_value=mock_client)
    mocker.patch('os.getenv', side_effect=['true', '/path/to/dummy/credentials.json', 'dummy_url'])

    # Mock ServiceAccountCredentials.from_json_keyfile_name
    mock_credentials = mocker.Mock()
    mocker.patch('oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_name', return_value=mock_credentials)

    result = load_from_google_sheets()
    assert isinstance(result, pd.DataFrame)
    assert 'Date' in result.columns
    assert 'Description' in result.columns
    assert 'Category' in result.columns
    assert 'Income/Expense' in result.columns
    assert 'Amount' in result.columns
