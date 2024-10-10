import pandas as pd
import pytest
from scripts.transaction_categorization import categorize_transactions

def test_categorize_transactions(mocker):
    mock_df = pd.DataFrame({
        'Description': ['Groceries at Walmart', 'Rent payment'],
        'Category': ['', ''],
        'Amount': [100, 1000]
    })

    # Mock the categorize_transaction function
    mocker.patch('scripts.transaction_categorization.categorize_transaction', side_effect=['Groceries', 'Housing'])

    # Mock the OpenAI API call (in case it's used directly in the categorize_transactions function)
    mock_completion = mocker.Mock()
    mock_completion.choices = [mocker.Mock(message=mocker.Mock(content="Mocked category"))]
    mocker.patch('openai.ChatCompletion.create', return_value=mock_completion)

    result = categorize_transactions(mock_df)

    assert result['Category'].tolist() == ['Groceries', 'Housing']
    assert len(result) == 2
    assert 'Description' in result.columns
    assert 'Category' in result.columns
    assert 'Amount' in result.columns
