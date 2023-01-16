def while_loop(lists: list) -> list:
    count = 0
    while count < len(lists):
        lists[count] *= 2
        count += 1
    return lists


if __name__ == '__main__':
    arrays = [23, 86, 34, 76]
    print(while_loop(arrays))
    