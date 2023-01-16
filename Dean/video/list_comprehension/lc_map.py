def lc_map(arrays: list) -> list:
    # this is a map example because it picks every elements in the list and
    # change their states and appending them to the list
    return [number ** 2 for number in arrays]


if __name__ == '__main__':
    numbers = [32, 43, 12, 34, 82, 56, 45]
    print(lc_map(numbers))
    # num = 10
    # while num > 0:
    #    print(num)
    #    num -= 1
    # print("end of loop")
    # print(num)#
