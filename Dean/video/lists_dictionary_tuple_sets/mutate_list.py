def double_elements(numbers: list) -> list:
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers


if __name__ == '__main__':
    num = [1, 2, 7, 3, 4, 5]
    print(double_elements(numbers=num))
