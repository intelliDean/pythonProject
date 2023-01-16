def for_sum(arrays: list) -> int:
    total = 0
    for number in arrays:
        total += number
    return total


def for_range_sum(arrays: list) -> int:
    total = 0
    for i in range(len(arrays)):
        total += arrays[i]
    return total


def while_sum(arrays: list) -> int:
    total = 0
    count = 0
    while count < len(arrays):
        total += arrays[count]
        count += 1
    return total


def enumerate_sum(arrays: list[int]) -> int:
    total = 0
    for index, number in enumerate(arrays):
        total += number
        # index is redundant cos it's of no use
    return total


if __name__ == '__main__':
    lists = [34, 65, 23, 65, 34]
    print(for_sum(lists))
    print(for_range_sum(lists))
    print(while_sum(lists))
    print(enumerate_sum(lists))
