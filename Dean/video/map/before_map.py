def even_list(numbers: list) -> list:
    # this part returns the square of each number in the list
    for i, j in enumerate(numbers):
        numbers[i] = j * j

    # this part returns only the even square in the list into a new empty list
    new_list = [] 
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)

    # the empty list is filled and returned
    return new_list


if __name__ == '__main__':
    number_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # a function that takes in a list of numbers, square the numbers and return only the
    # even numbers of the squared numbers
    print(even_list(number_array))
