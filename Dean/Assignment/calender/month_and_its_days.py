def tell_month_days(month):
    print(get_month_name(month), "has", get_number_of_days_in_month(month), "days")


def get_number_of_days_in_month(month):
    if (month == 1 or month == 3 or month == 5 or month == 7 or
            month == 8 or month == 10 or month == 12):
        return 31

    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30

    if month == 2:
        return 28, "29"

    return 0  # If month is incorrect


def get_month_name(month):
    if month == 1:
        month_name = "January"

    elif month == 2:
        month_name = "February"
    elif month == 3:
        month_name = "March"

    elif month == 4:
        month_name = "April"

    elif month == 5:
        month_name = "May"

    elif month == 6:
        month_name = "June"

    elif month == 7:
        month_name = "July"

    elif month == 8:
        month_name = "August"

    elif month == 9:
        month_name = "September"

    elif month == 10:
        month_name = "October"

    elif month == 11:
        month_name = "November"
    else:
        month_name = "December"
    return month_name


if __name__ == '__main__':
    a = eval(input("enter month and year, (e.g 4)\n"))
    tell_month_days(a)
