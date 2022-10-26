def list_comprehension(numbers):
    squares = [number ** 2 for number in numbers]
    return squares


def traditional_list(numbers):
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    return squares


if __name__ == '__main__':
    a = 3, 12, 15, 24, 20, 16  # this is a turple
    sqr = traditional_list(a)
    print(sqr)
