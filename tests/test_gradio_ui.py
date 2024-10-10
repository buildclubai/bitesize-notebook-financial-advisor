import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import pytest
from scripts.gradio_ui import advisor_interface

@pytest.fixture
def mock_df():
    return pd.DataFrame({
        'Description': ['Salary', 'Rent'],
        'Amount': [5000, 1000],
        'Income/Expense': ['Income', 'Expense'],
        'Category': ['Income', 'Housing']
    })

def test_advisor_interface_summary(mocker, mock_df):
    mocker.patch('scripts.financial_summary.generate_financial_summary', return_value="Mocked response")
    result = advisor_interface(mock_df, "Summary", 26, "", "")
    assert result == "Mocked response"

def test_advisor_interface_advice(mocker, mock_df):
    mocker.patch('scripts.financial_advice.generate_personalized_advice', return_value="Mocked response")
    result = advisor_interface(mock_df, "Advice", 26, "Urban", "Reading")
    assert result == "Mocked response"

def test_advisor_interface_invalid_question(mock_df):
    result = advisor_interface(mock_df, "Invalid", 26, "", "")
    assert "Please select either 'Summary' or 'Advice'." == result

def test_advisor_interface_default_age(mocker, mock_df):
    mocker.patch('scripts.financial_advice.generate_personalized_advice', return_value="Mocked response")
    result = advisor_interface(mock_df, "Advice", 26, "", "")
    assert result == "Mocked response"

def test_advisor_interface_optional_fields(mocker, mock_df):
    mocker.patch('scripts.financial_advice.generate_personalized_advice', return_value="Mocked response")
    result = advisor_interface(mock_df, "Advice", 26, "Urban", "")
    assert result == "Mocked response"
    result = advisor_interface(mock_df, "Advice", 26, "", "Reading")
    assert result == "Mocked response"
