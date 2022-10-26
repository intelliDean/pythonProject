import random

# random.seed(123)

number = random.randint(1, 100)

i = 1
while i <= 7:
    guess = int(input("\nGuess here\n"))
    if guess == number:
        print("Congratulations! You guessed", number, "right")
        break
    elif guess < number:
        print("It's lower. You have", 7 - i, "chances left")
    else:
        print("It is higher. You have", 7 - i, "chances left")
    i += 1
else:
    print("Ode, it's ordinary", number, "you cannot guess!")
