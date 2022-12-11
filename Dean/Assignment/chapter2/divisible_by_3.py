def divisible_by_3(number):
    return number % 3 == 0


if __name__ == '__main__':
    number = int(input("enter the number\n"))
    print(divisible_by_3(number))
