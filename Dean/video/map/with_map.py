def square_number(number: int) -> int:
    return number * 2


def square_list_with_function(numbers: list) -> list:
    # map takes a function declaration (without the parenthesis) not a function call
    mapping = map(square_number, numbers)  # square_number is the function declaration and numbers is the list passed
    # into the map
    return list(mapping)


def square_list_with_lambda(numbers: list) -> list:
    # map takes a function declaration (without the parenthesis) not a function call
    mapping = map(lambda num: num * 2, numbers)  # the lambda is the anonymous function and numbers is the list
    # passed into the map
    return list(mapping)


if __name__ == '__main__':
    arrays = [3, 54, 65, 89, 90]
    print(square_list_with_lambda(arrays))
    print(square_list_with_function(arrays))
