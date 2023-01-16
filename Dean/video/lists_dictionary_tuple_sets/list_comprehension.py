def list_comprehension(arrays: list) -> list:
    # for a number in arrays, if that number modulo 2 == 0 (even), add the number to the list
    return [number * 2 for number in arrays if number % 2 == 0]


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list_comprehension(numbers))
