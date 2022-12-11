def reverse(lists):
    new_list = []
    for i in reversed(lists):
        new_list.append(i)
    return new_list


if __name__ == '__main__':
    rays = [9, 8, 7, 6, 5]
    result = reverse(rays)
    print(result)
