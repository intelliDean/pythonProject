def range_test(number):
    for i in range(1, number + 1):
        print(i, end=" ")
        if i % 10 == 0:
            print()


if __name__ == '__main__':
    a = 20
    range_test(a)
