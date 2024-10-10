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
