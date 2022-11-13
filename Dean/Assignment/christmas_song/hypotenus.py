import math


def hypotenuse(a, b):
    if a > 1 and b > 1:
        c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
        return c


if __name__ == '__main__':
    base_1 = float(input("input base a\n"))
    base_2 = float(input("input base b\n"))
    d = hypotenuse(base_1, base_2)
    print(f"{d:.2f}")
