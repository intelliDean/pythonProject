def list_digits(num):
    res = []
    str_num = str(num)
    for i in str_num:
        res.append(i)
    return res


def digits(num):
    str_num = str(num)
    for i in str_num:
        print(i, end=" ")


if __name__ == '__main__':
    ans = int(input("enter number\n"))
    digits(ans)
