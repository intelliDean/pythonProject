def default(name="Dean", age=12):  # python allows default argument instead of method overloading
    if name == "Dean" and age == 20:
        print("Invalid identity")
    elif name == "Dean" and age == 10:
        print("correct identity")
    else:
        print("I no sabi this one o")


if __name__ == '__main__':
    default(name="Dean", age=10)  # you can also edit the arguments
