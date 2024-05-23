import random
import operator


def generate_question():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(list(operators.keys()))
    question = f"{num1} {op} {num2}"
    answer = operators[op](num1, num2)
    return question, answer


def brain_calc():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    correct_answers_count = 0
    questions_needed = 3

    while correct_answers_count < questions_needed:
        question, correct_answer = generate_question()
        print(f"Question: {question}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print(f"Invalid input. Please enter an integer.")
            continue

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    brain_calc()
