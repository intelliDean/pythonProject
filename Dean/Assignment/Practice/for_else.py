def for_else(word):
    for character in phrase:
        if character == "Y" or character == "y":
            print("y dey there")
            break
    else:
        print("There was no 'y' in the phrase")


if __name__ == '__main__':
    phrase = "sugar is all we ask that you include in the tea, not milk or more beverages"
    for_else(phrase)
