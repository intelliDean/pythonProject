def filter_even(lists: list) -> list:
    arrays = map(lambda num: num * num, lists)  # this maps and returns a list of the square of each number
    filtering = filter(lambda num: num % 2 == 0, arrays)  # this filter and return the list of only the even numbers
    # map performs the function duty on each elements of the list
    # filter filters the elements of the list that meets up with the condition of the function
    return list(filtering)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filter_even(numbers))
