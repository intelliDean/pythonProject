def for_in_range(number, word):
    for n in range(number):  # This loop will run for the amount of "number", starting from 0 to (number - 1)
        print(n, "- " + word)


if __name__ == '__main__':
    for_in_range(4, "Paradise")
