def bigger(num1: int, num2: int) -> int:  # take 2 ints and return an int
    big = num1
    if num2 > num1:
        big = num2
    return big


if __name__ == '__main__':
    print(bigger(230, 67))
