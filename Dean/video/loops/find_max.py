def find_max(numbers: list) -> int:
    maxim = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > maxim:
            maxim = numbers[i]
    return maxim


def find_max2(numbers: list) -> int:
    maxim = numbers[0]
    for number in numbers:
        if number > maxim:
            maxim = number
    return maxim


if __name__ == '__main__':
    lists = [34, 65, 23, 69, 34]
    print(find_max(lists))
    print(find_max2(lists))
