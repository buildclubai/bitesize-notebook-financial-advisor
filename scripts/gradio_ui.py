import gradio as gr
from financial_summary import generate_financial_summary
from financial_advice import generate_personalized_advice

def advisor_interface(df, question, age, lifestyle, hobbies):
    if "summary" in question.lower():
        return generate_financial_summary(df)
    elif "advice" in question.lower():
        return generate_personalized_advice(df, age, lifestyle, hobbies)
    else:
        return "I'm sorry, I didn't understand your question. Please ask for a summary or advice."

def launch_gradio_ui(df):
    iface = gr.Interface(
        fn=lambda q, a, l, h: advisor_interface(df, q, a, l, h),
        inputs=[
            gr.Textbox(label="Ask for a summary or advice"),
            gr.Number(label="Age"),
            gr.Textbox(label="Lifestyle"),
            gr.Textbox(label="Hobbies")
        ],
        outputs="text",
        title="AI Financial Advisor",
        description="Ask for a financial summary or personalized advice based on your transaction history."
    )
    iface.launch()
