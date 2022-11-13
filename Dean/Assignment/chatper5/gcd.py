def gcd(n1, n2):
    gcd_ = 1
    k = 2

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:

            gcd_ = k

        k += 1

    print("The GCD for", n1, "and", n2, "is", gcd_)


if __name__ == '__main__':
    num1 = eval(input("enter GCD num1\n"))
    num2 = eval(input("enter GCD num2\n"))
    gcd(num1, num2)
