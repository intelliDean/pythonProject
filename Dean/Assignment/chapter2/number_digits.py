def with_space(number):
    str_num = str(number)
    for i in str_num:
        print(i, end=" ")


if __name__ == '__main__':
    numbers = int(input("Enter number\n"))
    with_space(numbers)
