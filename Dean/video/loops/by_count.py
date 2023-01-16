def multiply_by_counter(numbers: list) -> list:
    count = 1
    while count <= len(numbers):
        numbers[count - 1] *= count
        count += 1
    return numbers


if __name__ == '__main__':
    arrays = [23, 43, 12, 89, 43]
    print(multiply_by_counter(numbers=arrays))

