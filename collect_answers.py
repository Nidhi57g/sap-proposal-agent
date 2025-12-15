def collect_answers(questions):
    answers = {}

    print("\n✍️ Please answer the following questions:\n")

    for q in questions:
        ans = input(f"{q}\n> ")
        answers[q] = ans

    return answers
