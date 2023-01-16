if __name__ == '__main__':
    print("print all even numbers in 20")
    for i in range(21):
        if i % 2 == 0 and i != 0:
            print(i, end=", ")

    print()

    for i in range(2, 21, 2):
        print(i, end=", ")

    print("\n\nprint all odd numbers in 20")

    for i in range(1, 21, 2):
        print(i, end=", ")

    print()

    for i in range(21):
        if i % 2 != 0:
            print(i, end=", ")

    print()
