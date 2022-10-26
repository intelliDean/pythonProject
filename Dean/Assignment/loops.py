def whileloop(number_of_loops):
    counter = 1
    while counter <= number_of_loops:
        print(counter, end=" ")
        counter += 1


def input_loop():
    num = float(input("Enter a positive number\n"))
    while num <= 0:
        print("That's not a positive number!")
        num = float(input("Enter a positive number\n"))


def count_with_while_loop():
    count = 1
    letter = "communication"
    while count <= len(letter):
        count += 1
    print(count)


def iterate_with_for_loop():
    for letter in "communication":
        print(letter.upper(), end=" ")


def repeat_with_range():
    for count in range(2, 11, 2):
        # if count % 2 == 0:
        print(count, end=" ")


def range_count():
    amount = float(input("Enter amount\n"))
    for number_of_people in range(2, 8):
        print(f"{number_of_people} People: ₦{amount / number_of_people:.2f} each")


def nested_loop():  # each of the nested loops are the column to the outer loop whilw each outer loops are the row to the inner loop
    for n in range(1, 4):
        for j in range(4, 7):
            for k in range(2, 4):
                for x in range(1, 11):
                    print(x, end=" ")
                print()
            # print(f"n = {n} and j = {j}")
            print()
        print()


# For example, a principal amount of $100 with an annual rate of return
# of 5% increases the first year by $5. The second year, the increase is
# 5% of the new amount $105, which is $5.25.
def invest(deposit, interest, year):
    interest = interest / 100
    count = 1
    print(f"Year 0 : ₦{deposit:.2f}")
    while count <= year:
        deposit = deposit + (deposit * interest)
        print(f"Year {count} : ₦{deposit:.2f}")
        count += 1


if __name__ == '__main__':
    dep = int(input("Enter the initial deposit\n"))
    inte = int(input("Enter the interest in integer\n"))
    yer = int(input("Enter the year\n"))
    invest(dep, inte, yer)
