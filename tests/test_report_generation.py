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

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.report_generation import create_pdf_report

def test_create_pdf_report(mocker):
    mock_pdfkit = mocker.patch('pdfkit.from_string')
    create_pdf_report("Mock summary", "Mock advice")
    mock_pdfkit.assert_called_once()
    args, kwargs = mock_pdfkit.call_args
    assert "Mock summary" in args[0]
    assert "Mock advice" in args[0]
    assert args[1] == 'financial_report.pdf'
