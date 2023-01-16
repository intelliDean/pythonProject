def freq(phase) -> dict:
    dict = {}
    for word in phase.split():
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict


if __name__ == '__main__':
    word = "i am a man of many faces also i am a man of many moods"
    print(freq(word))
