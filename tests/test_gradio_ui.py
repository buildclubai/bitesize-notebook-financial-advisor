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
from unittest.mock import Mock

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.gradio_ui import advisor_interface

@pytest.fixture
def mock_df():
    return {
        'Description': ['Salary', 'Rent'],
        'Amount': [5000, 1000],
        'Income/Expense': ['Income', 'Expense'],
        'Category': ['Income', 'Housing']
    }

def test_advisor_interface_summary(mocker, mock_df):
    mock_summary = mocker.patch('scripts.gradio_ui.generate_financial_summary', return_value="Mocked summary")
    result = advisor_interface(mock_df, "Summary", 26, "", "")
    assert result == "Mocked summary"
    mock_summary.assert_called_once_with(mock_df)

def test_advisor_interface_advice(mocker, mock_df):
    mock_advice = mocker.patch('scripts.gradio_ui.generate_personalized_advice', return_value="Mocked advice")
    result = advisor_interface(mock_df, "Advice", 26, "Urban", "Reading")
    assert result == "Mocked advice"
    mock_advice.assert_called_once_with(mock_df, 26, "Urban", "Reading")

def test_advisor_interface_invalid_question(mock_df):
    result = advisor_interface(mock_df, "Invalid", 26, "", "")
    assert result == "Invalid request type. Please choose 'Summary' or 'Advice'."

def test_advisor_interface_default_age(mocker, mock_df):
    mock_advice = mocker.patch('scripts.gradio_ui.generate_personalized_advice', return_value="Mocked advice")
    result = advisor_interface(mock_df, "Advice", 26, "", "")
    assert result == "Mocked advice"
    mock_advice.assert_called_once_with(mock_df, 26, "", "")

def test_advisor_interface_optional_fields(mocker, mock_df):
    mock_advice = mocker.patch('scripts.gradio_ui.generate_personalized_advice', return_value="Mocked advice")
    result = advisor_interface(mock_df, "Advice", 26, "Urban", "")
    assert result == "Mocked advice"
    mock_advice.assert_called_once_with(mock_df, 26, "Urban", "")
