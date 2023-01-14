def count_words(words: str) -> int:  # simple way
    split_word = words.split(" ")
    count = 0
    for i in split_word:
        count += 1
    return count


def word_count(words: str) -> int:  # simpler way
    return len(words.split())


words_count = lambda words: len(words.split())  # simplest way

if __name__ == '__main__':
    word = 'Holla, my name is Michael Dean Oyewole'
    print(words_count(words=word))
