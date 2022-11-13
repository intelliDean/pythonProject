def odd_position(lists):
    new_list = []
    count = 0
    for i in lists:
        if count % 2 == 1:
            new_list.append(i)
        count += 1
    return new_list


def odd_position_(lists):
    new = []
    new = lists[1::2]
    return new


if __name__ == '__main__':
    rays = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ans = odd_position(rays)
    print(ans)
