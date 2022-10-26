def factor_of_num(num):
    print(f"These are the factors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=", ")


if __name__ == '__main__':
    factor_of_num(21)
