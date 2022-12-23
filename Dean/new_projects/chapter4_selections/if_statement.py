number = eval(input("Enter an integer: "))

if number % 5 == 0:
    print("iFive!", int(number / 5), "times")
elif number % 2 == 0:
    print("HiEven!", int(number / 2), "times")
else:
    print("iOdd!")
