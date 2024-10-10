import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
import openai
from scripts.data_extraction import load_data
from financial_advice import generate_personalized_advice
from scripts.financial_summary import generate_financial_summary
from scripts.gradio_ui import launch_gradio_ui

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    # Check if the API key is set
    if not openai.api_key:
        print("Error: OpenAI API key is not set. Please check your .env file.")
        return

    # Load data
    df = load_data()

    try:
        # Generate financial summary
        summary = generate_financial_summary(df)

        # Generate personalized advice
        advice = generate_personalized_advice(df)

        # Launch Gradio UI
        launch_gradio_ui(df)
    except openai.error.AuthenticationError:
        print("Error: Invalid OpenAI API key. Please check your .env file and ensure the API key is correct.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
