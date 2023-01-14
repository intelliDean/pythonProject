def number_check(number):
    if number % 2 == 0 and number % 3 == 0:
        print(number, "is divisible by 2 and 3")

    if number % 2 == 0 or number % 3 == 0:
        print(number, "is divisible by 2 or 3")

    if (number % 2 == 0 or number % 3 == 0) and not (number % 2 == 0 and number % 3 == 0):
        print(number, "is divisible by 2 or 3, but not both")


if __name__ == '__main__':
    number_check(15)
