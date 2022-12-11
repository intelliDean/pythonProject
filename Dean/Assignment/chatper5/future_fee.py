def tuition(fee):
    year = 0  # Year 0
    accumulation = 0
    target = fee * 2
    if fee < 1000:
        accumulation = 1.10
    elif fee < 2000:
        accumulation = 1.08
    elif fee < 3000:
        accumulation = 1.05
    elif fee < 5000:
        accumulation = 1.03
    else:
        accumulation = 1.00
    while fee < target:
        year += 1
        fee *= accumulation
    print("Tuition will be doubled in", year, "years")
    print("Tuition will be ₦" + format(fee, ",.2f"), "in", year, "years")


if __name__ == '__main__':
    tuition(eval(input("enter tuition fee\n")))
