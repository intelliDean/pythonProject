def divide(num1, num2):
    try:
        print(num1 / num2)
    except (TypeError, ZeroDivisionError, ValueError):
        print("encountered a problem")


def divide(num2, num3):
    try:
        print(num2 / num3)
    except TypeError:
        print("Both arguments must be integers")
    except ZeroDivisionError:
        print(f"denominator must not be {num3}")


if __name__ == '__main__':
    divide(9, 0)
