def while_and_for_loop(num):
    n = 1
    while n <= num:
        print(n, end="  ")
        n += 1
    print()
    for i in range(2, num + 1, 1):
        print(i)


if __name__ == '__main__':
    while_and_for_loop(13)
