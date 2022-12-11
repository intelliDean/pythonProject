def for_loop(num, word):
    for i in num:
        print(i)
        for j in word:  # normal for loop
            print(j, end=",")
        print()


if __name__ == '__main__':
    int_list = [2, 4, 5, 6, 7]
    str_word = "Family"

    for_loop(int_list, str_word)
