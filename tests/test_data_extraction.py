import pandas as pd
import pytest
from scripts.data_extraction import load_data, load_from_csv, load_from_google_sheets

def test_load_data_csv(mocker):
    mocker.patch('os.getenv', return_value='false')
    mocker.patch('scripts.data_extraction.load_from_csv', return_value=pd.DataFrame({'test': [1, 2, 3]}))
    result = load_data()
    assert isinstance(result, pd.DataFrame)
    assert 'test' in result.columns

def test_load_data_google_sheets(mocker):
    mocker.patch('os.getenv', return_value='true')
    mocker.patch('scripts.data_extraction.load_from_google_sheets', return_value=pd.DataFrame({'test': [1, 2, 3]}))
    result = load_data()
    assert isinstance(result, pd.DataFrame)
    assert 'test' in result.columns

def test_load_from_csv(mocker):
    mock_csv = mocker.mock_open(read_data='Date,Amount\n2023-01-01,100\n2023-01-02,200')
    mocker.patch('builtins.open', mock_csv)
    mocker.patch('pandas.read_csv', return_value=pd.DataFrame({'Date': ['2023-01-01', '2023-01-02'], 'Amount': [100, 200]}))
    result = load_from_csv()
    assert isinstance(result, pd.DataFrame)
    assert 'Date' in result.columns
    assert 'Amount' in result.columns

def test_load_from_google_sheets(mocker):
    mock_sheet = mocker.Mock()
    mock_sheet.get_all_records.return_value = [{'Date': '2023-01-01', 'Amount': 100}, {'Date': '2023-01-02', 'Amount': 200}]
    mocker.patch('os.getenv', return_value='dummy_path')
    mocker.patch('oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_name', return_value=mocker.Mock())
    mocker.patch('gspread.authorize', return_value=mocker.Mock())
    mocker.patch('gspread.Client.open_by_url', return_value=mocker.Mock(sheet1=mock_sheet))
    result = load_from_google_sheets()
    assert isinstance(result, pd.DataFrame)
    assert 'Date' in result.columns
    assert 'Amount' in result.columns
