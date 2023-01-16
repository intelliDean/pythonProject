def word_frequency(words: str) -> dict:
    dict_word = {}
    new_word = words.split()
    count = 1
    for word in new_word:
        if word in dict_word:
            dict_word[word] += 1  # if the word already exist in the dict, just increase its value by 1
        else:
            dict_word[word] = 1  # if the word is not in the dict, give it a value of 1
    return dict_word


if __name__ == '__main__':
    print(word_frequency("I am Batman hence I love Batman"))
