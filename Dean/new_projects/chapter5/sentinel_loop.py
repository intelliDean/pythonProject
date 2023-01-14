data = eval(input("Enter an integer (the input ends " +
                  "if it is 0)\n-> "))

# Keep reading data until the input is 0
total = 0
while data != 0:
    total += data

    data = eval(input("-> "))

print("The sum is", total)
