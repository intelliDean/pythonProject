def single(taxable_income):
    if taxable_income <= 8350:
        return taxable_income * 0.1
    elif taxable_income <= 33950:
        return 8350 * 0.1 + (taxable_income - 8350) * 0.15
    elif taxable_income <= 82250:
        return 8350 * 0.1 + 33950 * 0.15 + (taxable_income - (33950 + 8350)) * 0.25
    elif taxable_income <= 171550:
        return 8350 * 0.1 + 33950 * 0.15 + 82250 * 0.25 + (taxable_income - (82250 + 33950 + 8350)) * 0.28
    elif taxable_income <= 372950:
        return 8350 * 0.1 + 33950 * 0.15 + 82250 * 0.25 + 171550 * 0.28 + (
                    taxable_income - (171550 + 82250 + 33950 + 8350)) * 0.33
    else:
        return 8350 * 0.1 + 33950 * 0.15 + 82250 * 0.25 + 171550 * 0.28 + 372950 * 0.33 + \
            (taxable_income - (372950 + 171550 + 82250 + 33950 + 8350)) * 0.35


def married_filing_jointly(taxable_income):
    # todo i will work on this later
    pass


def married_filing_separately(taxable_income):
    # todo i will work on this later
    pass


def head_of_house(taxable_income):
    # todo i will work on this later
    pass


def tax():
    filing_status = eval(input("enter your filing status\n"))
    taxable_income = eval(input("enter your taxable income\n"))
    if filing_status == 1:
        return single(taxable_income)
    elif filing_status == 2:
        return married_filing_jointly(taxable_income)
    elif filing_status == 3:
        return married_filing_separately(taxable_income)
    elif filing_status == 4:
        return head_of_house(taxable_income)
    else:
        return -1


if __name__ == '__main__':
    print(tax())
