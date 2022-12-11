def max_list(lists):
    if len(lists) == 0:
        return -1
    large = lists[0]
    for i in lists:
        if i > large:
            large = i
    return large


if __name__ == '__main__':
    arg = [54, 65, 34, 23, 76, 87, 34, 24, 65]
    result = max_list(arg)
    print(result)

