import math


def binary(number):
    total = 0
    i = 0
    while number > 0:
        rem = number % 10
        total += rem * math.pow(2, i)
        number /= 10
        i += 1
    return total


if __name__ == '__main__':
    number = 110011
    print(binary(number))
