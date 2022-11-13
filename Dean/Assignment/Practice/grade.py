if __name__ == '__main__':
    grade = int(input(" input grade"))
    if grade <= 39:
        print("E")
    elif grade <= 49:
        print("D")
    elif grade <= 69:
        print("C")
    elif grade <= 89:
        print("B")
    else:
        print("A")
