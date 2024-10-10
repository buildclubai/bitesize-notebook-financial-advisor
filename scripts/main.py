import os
from dotenv import load_dotenv
import openai
from scripts import (
    load_data,
    categorize_transactions,
    generate_financial_summary,
    generate_personalized_advice,
    create_pdf_report,
    launch_gradio_ui
)

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
