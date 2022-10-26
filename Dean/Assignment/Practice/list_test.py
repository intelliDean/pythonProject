def list_test(number):
    total = 0
    for i in number:
        total += i
    return total


if __name__ == '__main__':
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_total = list_test(lis)
    print(list_total)
