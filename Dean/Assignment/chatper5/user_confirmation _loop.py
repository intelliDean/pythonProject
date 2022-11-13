def user_loop():
    count = 1
    user_input = 'yes'
    while user_input == 'yes':
        num = eval(input("enter number\n"))
        print(num * count)
        count += 1
        user_input = input("would you like to continue?\nEnter Y to continue or N to quit\n")


if __name__ == '__main__':
    user_loop()
