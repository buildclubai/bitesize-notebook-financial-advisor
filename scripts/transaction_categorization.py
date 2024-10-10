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
