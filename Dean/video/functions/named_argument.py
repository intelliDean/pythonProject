def print_grade(name: str, score: float) -> str:
    return "Hello " + name + ", your score is " + str(score)


if __name__ == '__main__':
    print(print_grade(score=78, name="Dean"))
    # with named arguments, you can specifically name an argument when passing into a function with no order
