def even_position(lists):
    new_lists = []
    new_lists = lists[2::2]
    return new_lists


def even_position_(lists):
    new = []
    count = 0
    for i in lists:
        if count > 1 and count % 2 == 0:
            new.append(i)
        count += 1
    return new


if __name__ == '__main__':
    rays = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = even_position_(rays)
    print(result)
