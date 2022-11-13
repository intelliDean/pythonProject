def multiply(num):
    i = 1
    total = 1
    while i <= 12:
        total = i * num
        print(f"{i} x {num} = {total}")
        i += 1


if __name__ == '__main__':
    multiply(17)
