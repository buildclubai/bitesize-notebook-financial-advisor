import pandas as pd
import pytest
from scripts import load_data, load_from_csv, load_from_google_sheets

def test_load_data_csv(mocker):
    mocker.patch('os.getenv', return_value='false')
    mock_df = pd.DataFrame({'test': [1, 2, 3]})
    mocker.patch('scripts.data_extraction.load_from_csv', return_value=mock_df)
    result = load_data()
    assert isinstance(result, pd.DataFrame)
    assert 'test' in result.columns

def test_load_data_google_sheets(mocker):
    mocker.patch('os.getenv', return_value='true')
    mock_df = pd.DataFrame({'test': [1, 2, 3]})
    mocker.patch('scripts.data_extraction.load_from_google_sheets', return_value=mock_df)
    result = load_data()
    assert isinstance(result, pd.DataFrame)
    assert 'test' in result.columns

def test_load_from_csv(mocker):
    mock_df = pd.DataFrame({'Date': ['2023-01-01', '2023-01-02'], 'Amount': [100, 200]})
    mocker.patch('pandas.read_csv', return_value=mock_df)
    mocker.patch('os.path.join', return_value='dummy_path')
    result = load_from_csv()
    assert isinstance(result, pd.DataFrame)
    assert 'Date' in result.columns
    assert 'Amount' in result.columns

def test_load_from_google_sheets(mocker):
    mock_data = [
        {'Date': '2023-01-01', 'Amount': 100},
        {'Date': '2023-01-02', 'Amount': 200}
    ]
    mocker.patch('oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_name')
    mocker.patch('gspread.authorize')
    mock_client = mocker.Mock()
    mock_sheet = mocker.Mock()
    mock_sheet.get_all_records.return_value = mock_data
    mock_client.open_by_url.return_value.sheet1 = mock_sheet
    mocker.patch('gspread.authorize', return_value=mock_client)
    mocker.patch('os.getenv', side_effect=['dummy_path', 'dummy_url'])

    result = load_from_google_sheets()

    assert isinstance(result, pd.DataFrame)
    assert list(result.columns) == ['Date', 'Amount']
    assert len(result) == 2
    assert result['Amount'].sum() == 300
