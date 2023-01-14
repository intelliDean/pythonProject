from Dean.video.functions.bigger import bigger


def biggest(num1: int, num2: int, num3: int) -> int:
    return bigger(num1, bigger(num2, num3))


if __name__ == '__main__':
    print(biggest(53, 194, 161))
