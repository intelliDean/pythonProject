import datetime
import sys
from datetime import datetime


def withdraw():
    balance = 450000
    reply = eval(input("""
    Welcome!
    1.  check balance
    2.  deposit
    3.  withdraw
    4.  exit
    -> """))

    while reply != 4:
        if reply == 1:
            print(f"Your balance at {datetime.now()} is ₦{balance:,.2f}")
        if reply == 2:
            deposit_amount = eval(input("Enter the deposit amount: "))
            balance += deposit_amount
            print(f"Deposited successfully at {datetime.now()}\nYour new balance is ₦{balance:,.2f}")
        if reply == 3:
            withdraw_amount = eval(input("Enter the withdrawal amount: "))
            if withdraw_amount < balance:
                balance = balance - withdraw_amount
                print(f"Withdrawal successful at {datetime.now()}\nYour new balance is ₦{balance:,.2f}")
            else:
                print(f"Insufficient balance: ₦{balance:,.2f}")
        if reply == 4:
            sys.exit("Thank you for using our app")
        if reply < 1 or reply > 4:
            print("Invalid option")
        reply = eval(input("""
    1.  check balance
    2.  deposit
    3.  withdraw
    4.  exit
    -> """))


if __name__ == '__main__':
    withdraw()
