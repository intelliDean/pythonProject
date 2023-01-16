import math


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, (int(math.sqrt(number)) + 1)):
        if number % i == 0:
            return False
    return True


def prime_numbers(number: int) -> list:
    arrays = []
    for i in range(1, (number + 1)):
        if is_prime(i):
            arrays.append(i)
    return arrays


if __name__ == '__main__':
    lists = prime_numbers(59)
    print(lists)
