

def missing_value(lst):
    for i in range(1, len(lst)):
        if i not in lst:
            return i


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14,15]
    print(missing_value(arr))
