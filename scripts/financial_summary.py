# This file is part of bitesize-notebook-financial-advisor.
#
# AI Financial Advisor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AI Financial Advisor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AI Financial Advisor. If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (C) 2024 Vincent Koc (https://github.com/vincentkoc)
# Copyright (C) 2024 Hung Nguyen (https://github.com/hung-ngm)

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
