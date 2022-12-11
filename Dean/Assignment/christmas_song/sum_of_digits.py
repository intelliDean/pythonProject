def sum_of_digits(digits):
    global sum_digits
    str_digits = str(digits)
    spil = str_digits.split()
    print(spil)
    for n in spil:
        numbers = int(n)
        print(numbers)


if __name__ == '__main__':
    dig = int(input("enter digits\n"))
    sum_of_digits(dig)
