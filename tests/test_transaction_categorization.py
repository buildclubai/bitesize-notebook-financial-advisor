import pandas as pd
import pytest
from scripts.transaction_categorization import categorize_transactions, categorize_transaction

def test_categorize_transactions(mocker):
    mock_df = pd.DataFrame({
        'Description': ['Groceries at Walmart', 'Rent payment'],
        'Category': ['', ''],
        'Amount': [100, 1000]
    })
    mocker.patch('scripts.transaction_categorization.categorize_transaction', side_effect=['Groceries', 'Housing'])
    result = categorize_transactions(mock_df)
    assert result['Category'].tolist() == ['Groceries', 'Housing']

def test_categorize_transaction(mocker):
    mock_completion = mocker.Mock()
    mock_completion.choices = [mocker.Mock(message=mocker.Mock(content="Groceries"))]
    mocker.patch('openai.ChatCompletion.create', return_value=mock_completion)
    result = categorize_transaction("Groceries at Walmart")
    assert result == "Groceries"
