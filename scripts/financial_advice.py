import openai

def generate_personalized_advice(df, age, lifestyle, hobbies):
    try:
        largest_expense = df[df['Income/Expense'] == 'Expense'].nlargest(1, 'Amount')
        largest_expense_category = largest_expense['Category'].values[0] if not largest_expense.empty else "Unknown"
        largest_expense_amount = largest_expense['Amount'].values[0] if not largest_expense.empty else 0
    except KeyError:
        largest_expense_category = "Unknown"
        largest_expense_amount = 0

    prompt = f"Given a person aged {age} with a {lifestyle} lifestyle and interests in {hobbies}, " \
             f"their largest expense category is {largest_expense_category} at ${largest_expense_amount}. " \
             f"Provide personalized financial advice."

    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
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
