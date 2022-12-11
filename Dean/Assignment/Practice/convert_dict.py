def dico():
    values = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']
    keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    dic = {}

    for key in keys:
        for value in values:
            dic[key] = value
            return dic


if __name__ == '__main__':
    res = dico()
    print(res)
