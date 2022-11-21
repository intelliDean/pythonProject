def return_multiple(a, b, c):
    if a < b < c:
        return a, b, c
    elif a < c < b:
        return a, c, b
    elif b < a < c:
        return b, a, c
    elif b < c < a:
        return b, c, a
    elif c < a < b:
        return c, a, b
    elif c < b < a:
        return c, b, a


if __name__ == '__main__':
    print("sorting in an ascending order")
    first, second, third = return_multiple(23, 79, 65)
    print(first, second, third)
