import random

number1 = random.randint(1, 50)
number2 = random.randint(1, 50)

if number1 < number2:
    number1, number2 = number2, number1
reply = eval(input("What is " + str(number1) + " - " + str(number2) + " ?\n"))
result = number1 - number2

print(number1 - number2 == reply, "- answer =", result)
