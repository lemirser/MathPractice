# Pseudo code
"""
1. Ask user for difficulty (Basic, Easy, Medium, Hard).
2. Ask user for priority (Add, Subtraction, Multiplication, Division, Random).
3.

** Assume that the user's inputs are correct.
"""

import random

difficulty = input("Choose your difficulty level [Basic, Easy, Medium, Hard]: ")
operation = input("Choose the operation [+, -, *, /, Random]: ")


while True:

    a, b = 0, 0

    if difficulty == "basic":
        a = random.randint(0, 20)
        b = random.randint(0, 20)
    elif difficulty == "easy":
        a = random.randint(0, 40)
        b = random.randint(0, 40)
    elif difficulty == "medium":
        a = random.randint(0, 60)
        b = random.randint(0, 60)
    elif difficulty == "hard":
        a = random.randint(1, 100)
        b = random.randint(1, 100)

    rand_op = ["+", "*", "-", "/"]
    result = 0

    if operation == "random":
        operation = rand_op[random.randint(0, 3)]

    if operation == "+":
        print(f"{a} + {b}")
        result = a + b
    elif operation == "-":
        print(f"{a} - {b}")
        result = a - b
    elif operation == "*":
        print(f"{a} * {b}")
        result = a * b
    elif operation == "/":
        print(f"{a} / {b}")
        result = a / b

    _answer = input("Input your answer: ")

    if _answer == "exit":
        break

    if int(_answer) == int(result):
        print("Correct")
        print("\n" * 3)
    else:
        print("Incorrect, please try again!")
        print("\n" * 3)
