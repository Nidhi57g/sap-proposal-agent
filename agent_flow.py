from question_engine import generate_questions

def run_agent():
    print("\n🤖 SAP Proposal Agent Started\n")
    questions = generate_questions()

    if not questions:
        print("✅ No clarifications needed. Ready to generate proposal.")
        return

    print("🧠 The agent needs the following inputs:\n")
    for i, q in enumerate(questions, 1):
        print(f"{i}. {q}")

if __name__ == "__main__":
    run_agent()
