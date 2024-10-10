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
3. Set up your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY='your-api-key-here'
   ```
4. If using Google Sheets:
   - Set up Google Cloud Platform project and enable Google Sheets API
   - Create service account credentials and download the JSON key file
   - Set the path to your JSON key file as an environment variable:
     ```
     export GOOGLE_APPLICATION_CREDENTIALS='/path/to/your/credentials.json'
     ```

## Data

The project uses a synthetic dataset of financial transactions, available in two formats:
- CSV file: `data.csv` in the repository
- Google Sheets: [Public Google Sheet](https://docs.google.com/spreadsheets/d/1kuDZOyzT54yovmmF0pdWypIMPQQF6ZiX8VJGMecVyqI/edit?usp=sharing)

## Usage

Run the main script:

## License

This project is open-source and available under the MIT License.
