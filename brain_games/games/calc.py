import random
import operator

DESCRIPTION = "What is the result of the expression?"


def generate_question() -> object:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    op = random.choice(list(operations.keys()))
    question = f"{num1} {op} {num2}"
    correct_answer = str(operations[op](num1, num2))
    return question, correct_answer
