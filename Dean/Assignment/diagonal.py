def diagonal(lst: list) -> int:
    total = 0
    for i in range(len(lst)):
        total += lst[i][i]
    return total


if __name__ == '__main__':
    lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(diagonal(lists))
