def freq_letter(word: str) -> dict:
    dick = {}
    for letter in word:
        if letter not in dick:
            dick[letter] = 1
        else:
            dick[letter] += 1
    return dick


if __name__ == '__main__':
    word = "jdjsdjsdjjdkjjsdjdskjsdkj"
    print(freq_letter(word))
