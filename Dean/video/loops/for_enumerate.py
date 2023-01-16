def for_enumerate(lists: list) -> list:
    for i, j in enumerate(lists):
        lists[i] = j * 2
    return lists


if __name__ == '__main__':
    passed_lists = [43, 65, 67, 23]
    print(for_enumerate(passed_lists))
