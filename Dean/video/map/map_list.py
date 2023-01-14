def square_list(number_list: list[int]) -> list:
    # map takes a function declaration not a function call and also take the data it needs to work with
    return list(map(lambda num: num * num, number_list))


if __name__ == '__main__':
    numbers = [3, 2, 8, 5, 9]
    print(square_list(number_list=numbers))
    