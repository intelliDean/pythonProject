def add_numbers(number):
    if number < 1:
        return -1
    total = 0
    for i in range(12):
        if i != 0 and i % 2 == 0:
            total += i * number
    return total


