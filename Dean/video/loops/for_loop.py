def for_loop(lists: list[int]) -> list:
    for i in range(len(lists)):
        lists[i] = lists[i] * 2
    return lists


if __name__ == '__main__':
    lists = [43, 65, 21, 90, 54]
    new_list = for_loop(lists)
    print(new_list)

