def is_multiples(a, b):
    if a > 1 and b > 1:
        if b % a == 0:
            print(b, "is a multiple of", a)
        else:
            print(b, "is not a multiple of", a)
    else:
        print("invalid number")


if __name__ == '__main__':
    num1 = int(input("enter the number to be checked\n"))
    num2 = int(input("enter the number to check with\n"))
    is_multiples(num1, num2)
