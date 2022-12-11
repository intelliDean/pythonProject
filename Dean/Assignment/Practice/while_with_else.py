def while_else():
    n = 1
    guess = 23;
    while n <= 3:
        number = int(input("enter number\n"))
        if number == guess:
            print("Bravo! You are correct")
            break
        else:
            print(f"{3 - n} more tries")
            n += 1
    else:
        print(f"The number is {guess}")


if __name__ == '__main__':
    while_else()