from question_engine import generate_questions
from collect_answers import collect_answers

def run_agent():
    print("\n🤖 SAP Proposal Agent Started\n")

    questions = generate_questions()

    if not questions:
        print("✅ No clarifications needed.")
        return

    print("🧠 Clarification questions detected.")
    answers = collect_answers(questions)

    print("\n✅ Answers captured successfully.")
    for k, v in answers.items():
        print(f"- {k}: {v}")

if __name__ == "__main__":
    run_agent()
