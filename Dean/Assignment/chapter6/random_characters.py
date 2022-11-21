from random import randint  # import randint


def get_random_character(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


# Generate a random lowercase letter
def get_random_lowercase():
    return get_random_character('a', 'z')


# Generate a random uppercase letter
def get_random_uppercase():
    return get_random_character('A', 'Z')


# Generate a random digit character
def get_random_numbers():
    return get_random_character('0', '9')


# Generate a random character
def get_random_ascii_character():
    return chr(randint(0, 127))


if __name__ == '__main__':
    for i in range(26):
        print(get_random_lowercase(), end="  ")
        if (i + 1) % 13 == 0:
            print()
