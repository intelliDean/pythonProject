def find_value(value, arrays: list) -> bool:
    find = False
    for number in arrays:
        if value == number:
            find = True
            return find


def find_value_and_freq(value, arrays: list) -> list:
    find = False
    count = 0
    dick = {}
    for number in arrays:
        if value == number:
            find = True
            if number not in dick:
                dick[value] = 1
            else:
                dick[value] += 1
    return [find, dick]


if __name__ == '__main__':
    numbers = [23, 34, 12, 12, 12, 54, 43, 54, 23, 12, 12, 53]
    print(find_value(12, numbers))
    print(find_value_and_freq(12, numbers))
