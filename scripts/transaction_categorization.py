import openai

def categorize_transactions(df):
    for index, row in df[df['Category'] == ''].iterrows():
        category = categorize_transaction(row['Description'])
        df.at[index, 'Category'] = category
    return df

def categorize_transaction(description):
    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful financial assistant. Categorize transactions into one of the following categories: Groceries, Utilities, Rent, Entertainment, Transportation, Dining Out, Miscellaneous, Health & Fitness, Housing, Investments, Insurance, Charity, and Income."},
            {"role": "user", "content": f"Categorize the following transaction: '{description}'. Respond with the category name only."}
        ]
    )
    return completion.choices[0].message.content.strip()
