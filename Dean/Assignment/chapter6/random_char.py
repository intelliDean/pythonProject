import random


def rand_char():
    rand1 = random.randint(ord('a'), ord('z'))
    rand2 = random.randint(ord('A'), ord('Z'))
    rand3 = random.randint(ord('0'), ord('9'))

    char = chr(rand1)
    cap_char = chr(rand2)
    num_char = chr(rand3)
    print("lowercase", rand1, char, "|\n", "uppercase", rand2, cap_char, "|\n", "numbers", rand3, num_char)


if __name__ == '__main__':
    rand_char()
