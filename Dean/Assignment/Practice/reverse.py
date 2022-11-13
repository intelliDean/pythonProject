import math


def pizza_money(current, expected, fee):
    no_of_offender = (expected - current) / fee
    return math.ceil(no_of_offender)  # math.ceil will round off the number


if __name__ == '__main__':
    print("{} offenders remaining".format(pizza_money(4300, 27500, 100)))
    print("{} offenders remaining".format(pizza_money(4300, 27500, 200)))
    print("{} offenders remaining".format(pizza_money(4300, 27500, 500)))
    print("{} offenders remaining".format(pizza_money(4300, 27500, 1000)))
