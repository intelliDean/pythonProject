def largest_number(lists):
    largest = lists[0]
    for i in lists:
        if i > largest:
            largest = i
    return largest


if __name__ == '__main__':
    ray = [1, 2, 13, 3, 4, 7, 6, 5]
    result = largest_number(ray)
    print(f"The largest is {result}")

    lists_ = [89, 70, 56, 34, 87, 65]
    ans = max(lists_)
    print(f"The largest is {ans}")
