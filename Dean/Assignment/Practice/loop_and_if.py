def if_loop():
    sum_of_evens = 0
    for n in range(1, 100):
        if n % 2 == 0:
            print(n, end=" ")
            sum_of_evens += n
    print(f"\n{sum_of_evens}")


def loop_with_else(phrase, char):
    for character in phrase:
        if character == char:
            print(f"There was {char} in the phrase")
            break
    else:
        print(f"There was no {char} in the phrase")


def int_input_function():
    try:
        number = int(input("Enter an integer\n"))
    except ValueError:
        print("That was not an integer")


if __name__ == '__main__':
        # word = input("Enter word or phrase\n")
    # key = input("Enter character to search\n")
    # loop_with_else(word, key)
    int_input_function()
