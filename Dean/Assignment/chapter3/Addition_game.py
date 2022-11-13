import random


def game():
    number1 = random.randint(1, 10000)
    number2 = random.randint(1, 10000)

    # Prompt the user to enter an answer
    answer = eval(input(f"What is {number1:,} + {number2:,} ?\n"))

    add = number1 + number2

    if answer == add:
        print(f"You are correct! \n{number1:,} + {number2:,} = {answer:,} ")
    else:
        print(f"You are olodo osi! \n{number1:,} + {number2:,} is not {answer:,} ")


    #  Display result
    # print(f"{number1} + {number2} = {answer} \nthat's {number1 + number2 == answer}")


def range_game():
    num = random.randrange(2, 45)
    print(num)


if __name__ == '__main__':
    game()
