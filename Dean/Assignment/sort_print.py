def sort_print():
    number = input("enter number\n")
    new_number = sorted(number)
    word = input("enter word\n")
    new_word = sorted(word)
    word_list = list(new_word)
    number_list = list(new_number)
    print(f"word {word_list}\n number {number_list}")


if __name__ == '__main__':
    sort_print()
