def max_list(number_list: list[int]) -> int:  # simple
    big = number_list[0]
    for number in number_list:
        if number > big:
            big = number
    return big


def list_max(number_list: list) -> int:  # simpler
    return max(number_list)


max_of_list = lambda number_list: max(number_list)  # simplest


if __name__ == '__main__':
    numbers = [5, 3, 6, 4, 9]
    print(max_list(number_list=numbers))
