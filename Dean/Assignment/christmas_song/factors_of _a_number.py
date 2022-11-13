def factors(number):
    counter = 1
    while counter <= number:
        if number % counter == 0:
            print(counter, end=" ")
        counter += 1


def prime_number(num):
    counter = 1
    count = 0
    while counter <= num:
        if num % counter == 0:
            count += 1
        counter += 1
    if count > 2:
        print("\n{} is not a prime number".format(num))
    else:
        print("\n{} is a prime number".format(num))


if __name__ == '__main__':
    value = int(input("Enter number to determine it's factors\n"))
    factors(value)
