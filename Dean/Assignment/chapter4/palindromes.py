def palindrome(numbers):
    copied = numbers.copy()
    a = len(numbers) - 1
    b = 0
    while b < len(numbers) / 2:
        temp = numbers[b]
        numbers[b] = numbers[a]
        numbers[a] = temp
        a -= 1
        b += 1
    return numbers == copied


if __name__ == '__main__':
    lit = [2, 3, 4, 3, 2]
    print("Is it a palindrome number? ", palindrome(lit))


