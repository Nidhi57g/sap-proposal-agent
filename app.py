import gradio as gr
from agent_core import get_questions, run_agent_with_answers
from ppt_generator import generate_ppt

# Load questions once
questions = get_questions()

def generate_proposal(*answers):
    answer_dict = {questions[i]: answers[i] for i in range(len(questions))}
    slides = run_agent_with_answers(answer_dict)
    generate_ppt(slides)
    return "✅ Proposal generated successfully! Download generated_proposal.pptx from Files."

inputs = [gr.Textbox(label=q) for q in questions]

app = gr.Interface(
    fn=generate_proposal,
    inputs=inputs,
    outputs="text",
    title="SAP Proposal Agent",
    description="Answer the questions below to generate a SAP proposal PPT"
)

if __name__ == "__main__":
    app.launch()

