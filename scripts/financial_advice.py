import openai

def generate_personalized_advice(df, age=None, lifestyle=None, hobbies=None):
    largest_expense = df[df['Income/Expense'] == 'Expense'].nlargest(1, 'Amount')

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful financial assistant. Provide personalized financial advice based on the user's transaction history and personal information."},
            {"role": "user", "content": f"Based on the following information, provide personalized financial advice:\n"
                                        f"Largest expense: {largest_expense['Description'].values[0]} (${largest_expense['Amount'].values[0]:.2f})\n"
                                        f"Age: {age}\n"
                                        f"Lifestyle: {lifestyle}\n"
                                        f"Hobbies: {hobbies}"}
        ]
    )
    return completion.choices[0].message.content.strip()
