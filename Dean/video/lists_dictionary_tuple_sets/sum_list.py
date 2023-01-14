def sum_list(number_list: list) -> int:  # simple
    total = 0
    for number in number_list:
        total += number
    return total


def list_sum(number_list: list) -> int:  # simpler
    return sum(number_list)


sum_of_list = lambda number_list: sum(number_list)  # simplest

if __name__ == '__main__':
    numbers = [2, 3, 7, 5, 3, 2, 19]
    print(sum_of_list(number_list=numbers))
