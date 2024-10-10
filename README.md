# AI Financial Advisor

This project demonstrates how to build a personalized AI Financial Advisor using Python, OpenAI's GPT model, and Google Sheets or local CSV data. It's designed for people who want to learn some basics of AI, particularly those with existing Python knowledge or beginners in the field.

## Features

- Data extraction from Google Sheets or local CSV
- Transaction categorization using OpenAI's GPT model
- Generation of financial summaries and personalized advice
- PDF report generation
- Simple Gradio UI for interacting with the advisor

## Prerequisites

- Python 3.7+
- OpenAI API key
- Google Cloud Platform account with Google Sheets API enabled (if using Google Sheets)
- Required Python libraries (installed via pip)

## Setup

1. Clone this repository
2. Install required dependencies: `pip install -r requirements.txt`
3. Copy `example.env` to `.env` and update the values:
   ```
   cp example.env .env
   ```
4. Update the following variables in your `.env` file:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `GOOGLE_APPLICATION_CREDENTIALS`: Path to your Google Cloud credentials JSON file (if using Google Sheets)
   - `USE_GOOGLE_SHEETS`: Set to `true` if using Google Sheets, `false` if using local CSV
   - `DUMMY_DATA_SPREADSHEET`: URL of the dummy data Google Sheet (provided in the example.env)

## Data

The project uses a synthetic dataset of financial transactions, available in two formats:
- CSV file: `data.csv` in the repository
- Google Sheets: The URL is provided in the `DUMMY_DATA_SPREADSHEET` environment variable which comes from the following [Public Google Sheet](https://docs.google.com/spreadsheets/d/1kuDZOyzT54yovmmF0pdWypIMPQQF6ZiX8VJGMecVyqI/edit?usp=sharing).

## Usage

Run the main script:

```
python main.py
```

This will start the Gradio UI, allowing you to interact with the AI Financial Advisor.

## License

This project is open-source and available under the GPLv3 License.
