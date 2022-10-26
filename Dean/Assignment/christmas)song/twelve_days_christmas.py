def christmas_song(day):
    if 1 <= day <= 12:
        print("On the", day, end="")
        match day:
            case 1:
                print("st", end="")
            case 2:
                print("nd", end="")
            case 3:
                print("st", end="")
            case default:
                print("th", end="")
        print(" day of Christmas,\nmy true love gave to me")
        match day:
            case 12:
                print("Twelve drummers drumming,\n"
                      "Eleven pipers piping,\n"
                      "Ten lords a leaping\n"
                      "Nine ladies dancing\n"
                      "Eight maids a milking\n"
                      "Seven swans a swimming\n"
                      "Six geese a laying\n"
                      "Five golden rings\n"
                      "Four calling birds\n"
                      "Three french hens\n"
                      "Two turtle doves, and\n"
                      "a partridge in a pear tree")
            case 11:
                print("Eleven pipers piping,\n"
                      "Ten lords a leaping\n"
                      "Nine ladies dancing\n"
                      "Eight maids a milking\n"
                      "Seven swans a swimming\n"
                      "Six geese a laying\n"
                      "Five golden rings\n"
                      "Four calling birds\n"
                      "Three french hens\n"
                      "Two turtle doves, and\n"
                      "a partridge in a pear tree")
            case 10:
                print("Ten lords a leaping\n"
                      "Nine ladies dancing\n"
                      "Eight maids a milking\n"
                      "Seven swans a swimming\n"
                      "Six geese a laying\n"
                      "Five golden rings\n"
                      "Four calling birds\n"
                      "Three french hens\n"
                      "Two turtle doves, and\n"
                      "a partridge in a pear tree")
            case 9:
                print("Nine ladies dancing\n"
                      "Eight maids a milking\n"
                      "Seven swans a swimming\n"
                      "Six geese a laying\n"
                      "Five golden rings\n"
                      "Four calling birds\n"
                      "Three french hens\n"
                      "Two turtle doves, and\n"
                      "a partridge in a pear tree")
            case 8:
                print("Eight maids a milking\n"
                      "Seven swans a swimming\n"
                      "Six geese a laying\n"
                      "Five golden rings\n"
                      "Four calling birds\n"
                      "Three french hens\n"
                      "Two turtle doves, and\n"
                      "a partridge in a pear tree")
            case 7:
                print("Seven swans a swimming\n"
                      "Six geese a laying\n"
                      "Five golden rings\n"
                      "Four calling birds\n"
                      "Three french hens\n"
                      "Two turtle doves, and\n"
                      "a partridge in a pear tree")
            case 6:
                print("Six geese a laying\n"
                      "Five golden rings\n"
                      "Four calling birds\n"
                      "Three french hens\n"
                      "Two turtle doves, and\n"
                      "a partridge in a pear tree")
            case 5:
                print("Five golden rings\n"
                      "Four calling birds\n"
                      "Three french hens\n"
                      "Two turtle doves, and\n"
                      "a partridge in a pear tree")
            case 4:
                print("Four calling birds\n"
                      "Three french hens\n"
                      "Two turtle doves, and\n"
                      "a partridge in a pear tree")
            case 3:
                print("Three french hens\n"
                      "Two turtle doves, and\n"
                      "a partridge in a pear tree")
            case 2:
                print("Two turtle doves, and\n"
                      "a partridge in a pear tree")
            case default:
                print("a partridge in a pear tree")
    elif day == -1:
        print("")
    else:
        print("There is no", day, "of Christmas. Input between 1 and 12")


if __name__ == '__main__':
    day = int(input("Enter day of Christmas\nor press -1 to quit\n"))
    while day != -1:
        christmas_song(day)
        day = int(input())
