import random


def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_question():
    num = random.randint(1, 100)
    correct_answer = "yes" if is_prime(num) else "no"
    question = str(num)
    return question, correct_answer


def brain_prime():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers_count = 0
    questions_needed = 3

    while correct_answers_count < questions_needed:
        question, correct_answer = generate_question()
        print(f"Question: {question}")

        user_answer = input("Your answer: ").strip().lower()

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    brain_prime()
