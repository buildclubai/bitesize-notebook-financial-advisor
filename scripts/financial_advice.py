import openai
import pandas as pd

def generate_personalized_advice(df, age=None, lifestyle=None, hobbies=None):
    # Convert the dataframe to a string representation
    transactions = df.to_string(index=False)

    # Prepare the prompt
    prompt = f"""
    Based on the following transaction data:

    {transactions}

    And considering the following personal information:
    Age: {age}
    Lifestyle: {lifestyle}
    Hobbies: {hobbies}

    Please provide personalized financial advice. Include suggestions for budgeting, saving, and potential areas for improvement.
    """

    # Generate the advice using OpenAI's API
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful financial advisor."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract and return the generated advice
    return response.choices[0].message.content
