import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from report_generation import create_pdf_report

def test_create_pdf_report(mocker):
    mock_pdfkit = mocker.patch('pdfkit.from_string')
    create_pdf_report("Mock summary", "Mock advice")
    mock_pdfkit.assert_called_once()
    args, kwargs = mock_pdfkit.call_args
    assert "Mock summary" in args[0]
    assert "Mock advice" in args[0]
    assert args[1] == 'financial_report.pdf'
