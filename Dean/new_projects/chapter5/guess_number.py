import random

number = random.randint(1, 100)

guess = eval(input("Guess the number\n"))
count = 1
while count <= 3:
    print(number == guess)
    guess = eval(input("Guess the number again\n",))
    if guess > number:
        print("Your guess is too high")
    elif guess < number:
        print("Your guess is too low")
    else:
        print(guess == number, "- number is", number)
    count += 1
print("Try again later\n", "number was", number)
