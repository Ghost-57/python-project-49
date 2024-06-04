#!/usr/bin/env python3
import random


def is_even(num):
    return num % 2 == 0


def brain_even():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_count = 0
    questions_needed = 3

    while correct_answers_count < questions_needed:
        num = random.randint(1, 100)
        print(f"Question: {num}")
        correct_answer = "yes" if is_even(num) else "no"

        user_answer = input("Your answer: ").lower()

        if user_answer == correct_answer:
            print("correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    brain_even()
