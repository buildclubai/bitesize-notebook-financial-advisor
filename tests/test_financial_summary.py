import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import pytest
from financial_summary import generate_financial_summary

def test_generate_financial_summary(mocker):
    mock_df = pd.DataFrame({
        'Description': ['Salary', 'Rent', 'Groceries'],
        'Amount': [5000, 1000, 200],
        'Income/Expense': ['Income', 'Expense', 'Expense'],
        'Category': ['Income', 'Housing', 'Groceries']
    })
    mock_completion = mocker.Mock()
    mock_completion.choices = [mocker.Mock(message=mocker.Mock(content="This is a mock financial summary."))]
    mocker.patch('openai.ChatCompletion.create', return_value=mock_completion)

    result = generate_financial_summary(mock_df)
    assert isinstance(result, str)
    assert "This is a mock financial summary." in result
