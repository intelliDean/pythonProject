def dictionary(nth):
    dic = {}
    for i in range(1, nth + 1):
        dic[i] = {i * i}
    return dic


if __name__ == '__main__':
    result = dictionary(9)
    print(result)
