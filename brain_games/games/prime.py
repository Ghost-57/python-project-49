import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_question():
    num = random.randint(1, 100)
    question = str(num)
    correct_answer = "yes" if is_prime(num) else "no"
    return question, correct_answer
