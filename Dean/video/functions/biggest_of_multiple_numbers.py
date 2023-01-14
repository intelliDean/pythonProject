from Dean.video.functions.biggest import biggest


def biggest_multiple(num1: int, num2: int,
                     num3: int, num4: int, num5: int,
                     num6: int, num7: int) -> int:

    return biggest(num1, num2,
                   biggest(num3, num4,
                           biggest(num5, num6, num7)))


if __name__ == '__main__':
    print(biggest_multiple(234, 543, 7894, 764, 765, 234, 874))
