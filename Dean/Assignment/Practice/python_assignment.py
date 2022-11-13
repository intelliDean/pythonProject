def egg_box():  # 1
    box = 6
    eggs = 28
    number_of_boxes = (eggs // box) + 1
    rem = eggs % box
    print("\nYou need", number_of_boxes, "boxes to store", eggs, "eggs. \nHowever, the last box had only 2 eggs in it,"
                                                                 "\nremaining", rem, "to complete it", )


def bacteria_growth():  # 2
    bacteria = 200
    i = 0
    print("Hour"   "№ of bacteria")
    while i <= 15:
        number_of_growth = bacteria * 2 * i
        if i % 5 == 0:
            if i == 0:
                number_of_growth = 200
            print(i, number_of_growth)

        i += 1


def grade_print(grade):  # 3
    if grade > 90:
        print("\nCongratulations!\nYour grade of", grade, "earns you an A in this course")
    else:
        print("\nYour grade of", grade, "couldn't earn you an A\nbut you can do better next time")


def wage_calculator():  # 4
    import math
    i = 1
    wig = 0
    wage = 10
    good_job = 0
    while i <= 5:
        temp = 10 * 0.03
        wig = wage * math.pow(1 + temp, i)
        good_job += wig
        print(good_job)
        i += 1
    print("\n")

    wag = 0
    j = 1
    bad_job = 0
    while j <= 2:
        temp = 10 * 0.03
        wag = wage * math.pow(1 - temp, i)
        bad_job += wag
        print(bad_job)
        j += 1
    print("\n")

    print(good_job - bad_job)


def fibonacci(num):
    # int(input("Enter Fib number")
    a = 0  # a is initialized to 0
    b = 1  # b is initialized to 1
    i = 2
    while i <= num:
        c = b  # c is brought in to temporarily take the value of b
        b = a + b  # b is given value of a + b
        a = c  # a takes the former value of b stored in c
        print("\nThe ", num, "fibonacci number = ", b)
        i += 1


def heart_rate():




 def turing_test():
     problem = input('What is your problem? ')
     history = input(f'Have you had this problem {problem} before? (yes or no)')
     if history == 'yes':
         print('Then you have this problem again.')
     elif history == 'no':
         print('Well, you have it now.')
     elif history != 'yes' and history != 'no':
         while history != 'yes' and history != 'no':
             if history == 'yes' or history == 'no':
                 break
             else:
                 print('Please, enter yes or no')
                 history = input('Have you had this problem before?')
                 if history == 'yes':
                     print('Then you have this problem again.')
                 elif history == 'no':
                     print('Well, you have it now.')


def flu():
    total_cases = 0
    smallest_case = 9999999
    largest_case = 0
    for i in range(0, 7):
        cases = int(input('Enter the number of cases for the day: '))
        if cases < smallest_case:
            smallest_case = cases
        elif cases > largest_case:
            largest_case = cases
        total_cases += cases
    average_of_all_cases = total_cases / 7
    print(f'Total cases for week is {total_cases}')
    print(f'Average cases for week is {average_of_all_cases}')
    print(f'Smallest case is {smallest_case}')
    print(f'Largest case is {largest_case}')

def equilateral_triangle(side_1, side_2, side_3):
    if side_1 == side_2 and side_2 == side_3:
        print('Equilateral triangle')
    else:
        print('Not an equilateral triangle')

def palindrome(number):
    temp = number
    summation = 0
    while number != 0:
        rem = number % 10
        summation = (summation * 10) + rem
        number //= 10
    if summation == temp:
        print('It is a palindrome number')
    else:
        print('It is not a palindrome number')

def extract(number):
    while number != 0:
        rem = number % 10
        number //= 10
        print(rem, end=' ')

def multiplication_table():
    for number in range(1, 11):
        for multiply in range(1, 10):
            print(number * multiply, end=' ')
        print('\n')





if __name__ == '__main__':
    egg_box()
    multiplication_table()
    extract(12)
    palindrome(12321)
    equilateral_triangle(2,6,8)
    flu()
    heart_rate()
    fibonacci(12)
    wage_calculator()
    grade_print(89)
    bacteria_growth()
    egg_box()

