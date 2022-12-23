import random

number1 = random.randint(1, 50)
number2 = random.randint(1, 50)

reply = eval(input("what is " + str(number1) + " + " + str(number2) + " ?\n"))
result = number1 + number2
print(number1 + number2 == reply, "- answer =", result)


