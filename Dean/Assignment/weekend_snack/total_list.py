def total_lists(lists):
    total = 0
    for i in lists:
        total += i
    return total


def total_sum(lists):
    count = 0
    total = 0
    while count < len(lists):
        total += lists[count]
        count += 1
    return total


if __name__ == '__main__':
    rays = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = total_sum(rays)
    print(result)
