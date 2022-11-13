def sum_with_while(number):
    total = 0
    count = 1
    while count <= number:
        total += count
        count += 1
    print(f"{total:,}")


if __name__ == '__main__':
    sum_with_while(eval(input("enter number\n")))
