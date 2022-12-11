def input_numbers():
    try:
        number = int(input("Enter an integer\n"))
        print("added successfully")
    except ValueError:
        print("Ode, that was not an integer")


if __name__ == '__main__':
    input_numbers()
