from question_engine import generate_questions
from collect_answers import collect_answers
from proposal_builder import build_outline
from ppt_generator import generate_ppt

def run_agent():
    print("\n🤖 SAP Proposal Agent Started\n")

    questions = generate_questions()
    answers = collect_answers(questions)

    print("\n🛠 Building proposal outline...")
    slides = build_outline(answers)

    print("\n📊 Generating PPT...")
    generate_ppt(slides)

if __name__ == "__main__":
    run_agent()
