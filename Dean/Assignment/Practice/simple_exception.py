def simple_exception():
    try:
        number = int(input("enter number\n"))
        number += 42
        return number
    except:
        return "you don do rubbish"


if __name__ == '__main__':
    ex = simple_exception()
    print(ex)