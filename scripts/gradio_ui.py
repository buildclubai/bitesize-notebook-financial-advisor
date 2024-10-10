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

import gradio as gr
from scripts.financial_summary import generate_financial_summary
from scripts.financial_advice import generate_personalized_advice

def advisor_interface(df, request_type, age, location, hobbies):
    if request_type == "Summary":
        return generate_financial_summary(df)
    elif request_type == "Advice":
        return generate_personalized_advice(df, age=age, lifestyle=location, hobbies=hobbies)
    else:
        return "Invalid request type. Please choose 'Summary' or 'Advice'."

def launch_gradio_ui(df):
    iface = gr.Interface(
        fn=lambda q, a, l, h: advisor_interface(df, q, a, l, h),
        inputs=[
            gr.Dropdown(
                choices=["Summary", "Advice"],
                label="Select summary or advice"
            ),
            gr.Number(label="Age"),
            gr.Textbox(label="Lifestyle (optional)", placeholder="e.g., Urban, Rural, Suburban"),
            gr.Textbox(label="Hobbies (optional)", placeholder="e.g., Reading, Sports, Travel")
        ],
        outputs="text",
        title="AI Financial Advisor",
        description="Get a financial summary or personalized advice based on your transaction history."
    )
    iface.launch()
