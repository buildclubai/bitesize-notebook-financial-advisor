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
# Copyright (C) 2024 Hung Nguyen (https://github.com/hung-ngm)

import pdfkit

def create_pdf_report(summary, advice, output_path='financial_report.pdf'):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Financial Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            h1 {{ color: #2c3e50; text-align: center; }}
            h2 {{ color: #34495e; }}
            h3 {{ color: #2980b9; }}
            .section {{ margin-bottom: 20px; }}
            ul {{ padding-left: 20px; }}
        </style>
    </head>
    <body>
        <h1>Financial Report</h1>

        <div class="section">
            <h2>Financial Summary</h2>
            {0}
        </div>

        <div class="section">
            <h2>Personalized Financial Advice</h2>
            {1}
        </div>
    </body>
    </html>
    """.format(
        summary.replace('**', '').replace('###', '<h3>').replace('\n', '<br>'),
        advice.replace('**', '').replace('###', '<h3>').replace('\n', '<br>')
    )

    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
    }

    pdfkit.from_string(html_content, output_path, options=options)
    print(f"PDF report generated: {output_path}")
