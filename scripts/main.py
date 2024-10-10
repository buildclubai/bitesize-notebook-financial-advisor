import os
from dotenv import load_dotenv
import openai
from scripts.data_extraction import load_data
from scripts.transaction_categorization import categorize_transactions
from scripts.financial_summary import generate_financial_summary
from scripts.financial_advice import generate_personalized_advice
from scripts.report_generation import create_pdf_report
from scripts.gradio_ui import launch_gradio_ui

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    # Load data
    df = load_data()

    # Categorize transactions
    df = categorize_transactions(df)

    # Generate financial summary
    summary = generate_financial_summary(df)

    # Generate personalized advice
    advice = generate_personalized_advice(df)

    # Create PDF report
    create_pdf_report(summary, advice)

    # Launch Gradio UI
    launch_gradio_ui(df)

if __name__ == "__main__":
    main()
