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
