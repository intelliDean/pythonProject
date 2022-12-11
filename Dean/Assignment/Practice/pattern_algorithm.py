def pattern():
    column_length = 20
    row_length = 10
    row = 1
    while row <= row_length:
        row += 1
        column = 1
        while column <= column_length:
            if row == 1 | row == row_length | column == 1 | column == column_length:
                print('*')
            else:
                print(' ')
        print()
        column += 1

