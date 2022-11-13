def vowels(word):
    for i in word:
        for j in i:
            if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
                print(j, end=" ")


if __name__ == '__main__':
    vowels(input("Enter phrase\n"))
