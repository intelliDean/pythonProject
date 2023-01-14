def leap_year(year):
    # Check if the year is a leap year
    is_leap_year = (year % 4 == 0 and year % 100 != 0) \
                   or (year % 400 == 0)

    # Display the result
    print("is", year, "a leap year?", is_leap_year)


if __name__ == '__main__':
    leap_year(eval(input("enter year\n")))
