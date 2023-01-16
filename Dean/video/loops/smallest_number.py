def smallest_number(arrays: list) -> int:
    smallest = None
    for number in arrays:
        if smallest is None:
            smallest = number
        elif smallest > number:
            smallest = number
    return smallest


def smallest_number1(arrays: list) -> int:
    smallest = arrays[0]
    for i in range(1, len(arrays)):
        if arrays[i] < smallest:
            smallest = arrays[i]
    return smallest


def smallest_number2(arrays: list) -> int:
    smallest = arrays[0]
    i = 1
    while i < len(arrays):
        if smallest > arrays[i]:
            smallest = arrays[i]
        i += 1
    return smallest


if __name__ == '__main__':
    numbers = [2, 34, 64, 12, 9, -17]
    print(smallest_number(numbers))
    print(smallest_number1(numbers))
    print(smallest_number2(numbers))
