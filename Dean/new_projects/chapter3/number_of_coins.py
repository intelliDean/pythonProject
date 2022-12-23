def money_change(amount):
    # Convert the amount to cents
    remaining_amount = int(amount * 100)

    # Find the number of one dollars
    number_of_one_dollars = remaining_amount // 100
    remaining_amount = remaining_amount % 100

    # Find the number of quarters in the remaining amount
    number_of_quarters = remaining_amount // 25
    remaining_amount = remaining_amount % 25

    # Find the number of dimes in the remaining amount
    number_of_dimes = remaining_amount // 10
    remaining_amount = remaining_amount % 10

    # Find the number of nickels in the remaining amount
    number_of_nickels = remaining_amount // 5
    remaining_amount = remaining_amount % 5

    # Find the number of pennies in the remaining amount
    number_of_pennies = remaining_amount

    # Display the results
    print("Your amount", amount, "consists of\n",
          "\t", number_of_one_dollars, "dollars\n",
          "\t", number_of_quarters, "quarters\n",
          "\t", number_of_dimes, "dimes\n",
          "\t", number_of_nickels, "nickels\n",
          "\t", number_of_pennies, "pennies")


if __name__ == '__main__':
    # Receive the amount
    amount = eval(input("Enter an amount, for example, 11.56\n"))
    money_change(amount)
