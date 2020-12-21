# Pseudo code
"""
1. Ask user for difficulty (Basic, Easy, Medium, Hard).
2. Ask user for priority (Add, Subtraction, Multiplication, Division, Random).
3.

** Assume that the user's inputs are correct.
"""

import random

print(random.randint(0, 10))


def user_input():
    difficulty = input("Choose your difficulty level [Basic, Easy, Medium, Hard]: ")
    operation = input("Choose the operation [+, -, *, /, Random]: ")
    return (difficulty.lower(), operation.lower())


def diff_level():
    level, op = user_input()
    result, a, b = 0, 0, 0
    rand_op = ["+", "*", "-", "/"]

    if level == "basic":
        a = random.randint(0, 20)
        b = random.randint(0, 20)
    elif level == "easy":
        a = random.randint(0, 40)
        b = random.randint(0, 40)
    elif level == "medium":
        a = random.randint(0, 60)
        b = random.randint(0, 60)
    elif level == "hard":
        a = random.randint(1, 100)
        b = random.randint(1, 100)

    if op == "random":
        op = rand_op[random.randint(0, 3)]

    if op == "+":
        print(f"{a} + {b}")
        result = a + b
    elif op == "-":
        print(f"{a} - {b}")
        result = a - b
    elif op == "*":
        print(f"{a} * {b}")
        result = a * b
    elif op == "/":
        print(f"{a} / {b}")
        result = a / b

    return result


print(diff_level())
