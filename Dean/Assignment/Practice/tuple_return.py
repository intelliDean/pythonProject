def tuple_returns(num1, num2, num3, num4):
    a = num1 + num2
    b = num3 + num4
    c = a - b
    d = min(a, b)
    e = max(a, b)
    f = (a + b) / d
    g = (a + b) / e
    return a, b, c, d, e, f, g


if __name__ == '__main__':
    t = tuple_returns(34, 23, 78, 12)
    print(t)
