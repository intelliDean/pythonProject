def count_word(word: str) -> int:
    return len(word.split())


if __name__ == '__main__':
    string = "My name is Dean and i am a software engineer"
    print(count_word(word=string))
