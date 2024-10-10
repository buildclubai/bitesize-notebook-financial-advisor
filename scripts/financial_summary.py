import openai

def generate_financial_summary(df):
    total_spent = df[df['Income/Expense'] == 'Expense']['Amount'].sum()
    total_income = df[df['Income/Expense'] == 'Income']['Amount'].sum()
    category_spending = df[df['Income/Expense'] == 'Expense'].groupby('Category')['Amount'].sum()

    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful financial assistant. Generate a concise financial summary based on the provided data."},
            {"role": "user", "content": f"Generate a financial summary based on the following data:\n"
                                        f"Total Income: ${total_income:.2f}\n"
                                        f"Total Expenses: ${total_spent:.2f}\n"
                                        f"Spending by category: {category_spending.to_dict()}"}
        ]
    )
    return completion.choices[0].message.content.strip()
