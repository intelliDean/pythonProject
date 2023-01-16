def largest_number(arrays: list) -> int:
    largest = None
    for number in arrays:
        if largest is None:
            largest = number
        elif largest < number:
            largest = number
    return largest


def largest_number2(arrays: list) -> int:
    largest = arrays[0]
    for i in range(1, len(arrays)):
        if arrays[i] > largest:
            largest = arrays[i]
    return largest


def largest_number3(arrays: list) -> int:
    largest = arrays[0]
    i = 1
    while i < len(arrays):
        if arrays[i] > largest:
            largest = arrays[i]
        i += 1
    return largest


if __name__ == '__main__':
    numbers = [-12, -43, -34, -23, -65, -45, -76, -87, -45, -75]
    print(largest_number(numbers))
    print(largest_number2(numbers))
    print(largest_number3(numbers))
