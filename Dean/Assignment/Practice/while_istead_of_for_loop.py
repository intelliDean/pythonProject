def while_instead_for(word):  # Stressful, longer line of codes and more complex
    index = 0
    while index < len(word):
        print(word[index], end=", ")
        index += 1


def compare_for_to_while(word):     # More efficient and simple
    for index in word:
        print(index, end=", ")


if __name__ == '__main__':
    phrase = "Kingdom of God"
    compare_for_to_while(phrase)
