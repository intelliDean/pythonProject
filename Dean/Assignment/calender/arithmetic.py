def square_two_numbers(a, b):
    return a * a, b * b


def sum_square(a, b):
    return (a * a) + (b * b)


def square_differences(a, b):
    return (a * a) - (b * b)


if __name__ == '__main__':
    print(square_two_numbers(2, 3))
    print(sum_square(3, 5))
    print(square_differences(6, 3))
