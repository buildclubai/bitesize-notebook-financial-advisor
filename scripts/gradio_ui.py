import gradio as gr
from scripts.financial_summary import generate_financial_summary
from scripts.financial_advice import generate_personalized_advice

def advisor_interface(df, question_type, age, lifestyle, hobbies):
    if question_type == "Summary":
        return generate_financial_summary(df)
    elif question_type == "Advice":
        return generate_personalized_advice(df, age, lifestyle, hobbies)
    else:
        return "Please select either 'Summary' or 'Advice'."

def launch_gradio_ui(df):
    iface = gr.Interface(
        fn=lambda q, a, l, h: advisor_interface(df, q, a, l, h),
        inputs=[
            gr.Dropdown(
                choices=["Summary", "Advice"],
                label="Select summary or advice"
            ),
            gr.Number(label="Age", default=26),
            gr.Textbox(label="Lifestyle (optional)", placeholder="e.g., Urban, Rural, Suburban"),
            gr.Textbox(label="Hobbies (optional)", placeholder="e.g., Reading, Sports, Travel")
        ],
        outputs="text",
        title="AI Financial Advisor",
        description="Get a financial summary or personalized advice based on your transaction history."
    )
    iface.launch()
