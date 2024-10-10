import pdfkit

def create_pdf_report(summary, advice):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Monthly Financial Report</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
            }}
        </style>
    </head>
    <body>
        <h1 style="text-align: center;">Monthly Financial Report</h1>

        <h2>Summary</h2>
        {summary}

        <h2>Advice</h2>
        {advice}
    </body>
    </html>
    """

    options = {
        'encoding': 'UTF-8',
    }

    pdfkit.from_string(html_content, 'financial_report.pdf', options=options)
