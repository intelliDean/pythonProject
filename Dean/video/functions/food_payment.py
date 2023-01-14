def calc():
    food_amount = eval(input("enter food amount: ₦"))
    tip_perc = eval(input("enter tip percentage: %")) / 100
    tip_amount = tip_perc * food_amount
    total = food_amount + tip_amount
    print("------------------------------------------")
    print(f"Food amount is ₦{food_amount:,.2f}")
    print(f"Tip amount is ₦{tip_amount:,.2f}")
    print(f"Total payment = ₦{total:,.2f}")
    print("------------------------------------------")

    print("------------------------------------------")
    print("Food amount is ₦" + str(format(food_amount, ",.2f")))
    print("Tip amount is ₦" + str(format(tip_amount, ",.2f")))
    print("Total payment = ₦" + str(format(total, ",.2f")))
    print("------------------------------------------")


if __name__ == '__main__':
    calc()
