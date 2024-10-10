import pandas as pd
import pytest
from scripts.gradio_ui import advisor_interface

def test_advisor_interface_summary(mocker):
    mock_df = pd.DataFrame({
        'Description': ['Salary', 'Rent'],
        'Amount': [5000, 1000],
        'Income/Expense': ['Income', 'Expense'],
        'Category': ['Income', 'Housing']
    })
    mocker.patch('scripts.financial_summary.generate_financial_summary', return_value="Mock summary")
    result = advisor_interface(mock_df, "Summary", 26, "", "")
    assert result == "Mock summary"

def test_advisor_interface_advice(mocker):
    mock_df = pd.DataFrame({
        'Description': ['Salary', 'Rent'],
        'Amount': [5000, 1000],
        'Income/Expense': ['Income', 'Expense'],
        'Category': ['Income', 'Housing']
    })
    mocker.patch('scripts.financial_advice.generate_personalized_advice', return_value="Mock advice")
    result = advisor_interface(mock_df, "Advice", 26, "Urban", "Reading")
    assert result == "Mock advice"

def test_advisor_interface_invalid_question():
    mock_df = pd.DataFrame({'test': [1, 2, 3]})
    result = advisor_interface(mock_df, "Invalid", 26, "", "")
    assert "Please select either 'Summary' or 'Advice'." in result

def test_advisor_interface_default_age():
    mock_df = pd.DataFrame({'test': [1, 2, 3]})
    mocker.patch('scripts.financial_advice.generate_personalized_advice', return_value="Mock advice")
    result = advisor_interface(mock_df, "Advice", 26, "", "")
    assert result == "Mock advice"

def test_advisor_interface_optional_fields():
    mock_df = pd.DataFrame({'test': [1, 2, 3]})
    mocker.patch('scripts.financial_advice.generate_personalized_advice', return_value="Mock advice")
    result = advisor_interface(mock_df, "Advice", 26, "Urban", "")
    assert result == "Mock advice"
    result = advisor_interface(mock_df, "Advice", 26, "", "Reading")
    assert result == "Mock advice"
