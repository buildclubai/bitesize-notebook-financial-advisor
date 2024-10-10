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

import sys
import os
import pytest
import pandas as pd

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.financial_summary import generate_financial_summary

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
