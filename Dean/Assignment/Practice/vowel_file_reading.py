def read_vowel(word):
    vowel_str = "aeiou"
    vowel_space = ""
    for char in word:
        if char in vowel_str:
            vowel_space += char
    return vowel_space


if __name__ == '__main__':
    read = open("vowel_file.txt", "r")
    print(read_vowel(read))
    read.close()
