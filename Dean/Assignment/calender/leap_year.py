def leap_year(year):
    num_str = str(year)
    if len(num_str) < 4:
        print("invalid year")
    elif is_leap_lear(year):
        print(year, "was a leap year "if year <= 2022 else "is a leap year")
    else:
        print(year, "was not a leap year" if year <= 2022 else "is not be a leap year")


def is_leap_lear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


if __name__ == '__main__':
    year_ = eval(input("enter year in full, e.g. 2011\n"))
    leap_year(year_)
