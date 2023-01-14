import random
import time

correctCount = 0  # Count the number of correct answers
count = 0  # Count the number of questions
NUMBER_OF_QUESTIONS = 5  # Constant

startTime = time.time()  # Get start time

while count < NUMBER_OF_QUESTIONS:

    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    if number1 < number2:
        number1, number2 = number2, number1

    answer = eval(input("What is " + str(number1) + " - " + str(number2) + "?\n"))
    result = number1 - number2

    if result == answer:
        print("You are correct!")
        correctCount += 1
    else:
        print("Your answer is wrong.\n", number1, "-", number2, "=", result)

# Increase the count
    count += 1

endTime = time.time()  # Get end time
testTime = int(endTime - startTime)  # Get test time
print("You scored", correctCount, "over", NUMBER_OF_QUESTIONS, "in", testTime, "seconds")
