import random

DESCRIPTION = "Answer 'yes' if the number is even, otherwise answer 'no'."


def is_even(num):
    return num % 2 == 0


def generate_question():
    num: int = random.randint(1, 100)
    question = str(num)
    correct_answer = "yes" if is_even(num) else "no"
    return question, correct_answer
