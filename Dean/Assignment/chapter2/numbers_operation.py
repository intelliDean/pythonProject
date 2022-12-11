def adding_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def average(numbers):
    total = adding_numbers(numbers)
    return total / len(numbers)


def multiply(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


def max_number(numbers):
    maxim = numbers[0]
    for number in numbers:
        if number > maxim:
            maxim = number
    return maxim


def min_number(numbers):
    minim = numbers[0]
    for number in numbers:
        if number < minim:
            minim = number
    return minim


if __name__ == '__main__':
    num1 = int(input("Enter numbers 1\n"))
    num2 = int(input("Enter numbers 2\n"))
    num3 = int(input("Enter numbers 3\n"))
    numbers = (num1, num2, num3)

    print(f"sum {adding_numbers(numbers):,}")
    print(f"average {average(numbers):.2f}")
    print(f"product {multiply(numbers):,}")
    print("max", max_number(numbers))
    print("min", min_number(numbers))

