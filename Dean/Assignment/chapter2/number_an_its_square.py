def number_and_its_square(number):
    square = number * number
    number_and_square = square + number
    COMP = 100
    if number_and_square > COMP:
        return 1
    elif number_and_square < COMP:
        return -1
    else:
        return 0


def number_and_square(number):
    square = number * number
    number_and_square = square + number
    COMP = 100
    if number_and_square > COMP:
        print(f"{number} and its square, {square} > {COMP}")
    elif number_and_square < COMP:
        print(f"{number} and its square, {square} < {COMP}")
    else:
        print(f"{number} and its square, {square} = {COMP}")


if __name__ == '__main__':
    number = eval(input("enter number\n"))
    print(number_and_its_square(number))
    number_and_square(number)
