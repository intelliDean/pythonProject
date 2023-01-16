def lc_filter(array: list) -> list:
    # for number in array, if that number % 2 == 0, multiply the number by 2 and append the number in the list
    # thus is filter because it only picks the even numbers and perform the tasks on them
    return [number * 2 for number in array if number % 2 == 0]


if __name__ == '__main__':
    numbers = [23, 54, 34, 89, 13, 78, 54, 9, 90]
    print(lc_filter(numbers))
