def leap_year(year):
    isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    print(f"is {year} a leap year? \n{isLeapYear}")


if __name__ == '__main__':
    check_year = eval(input("input year\n"))
    leap_year(check_year)
