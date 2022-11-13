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
        while day > 0:
            match day:
                case 12:
                    print("Twelve drummers drumming,")
                case 11:
                    print("Eleven pipers piping,")
                case 10:
                    print("Ten lords a leaping,")
                case 9:
                    print("Nine ladies dancing,")
                case 8:
                    print("Eight maids a milking,")
                case 7:
                    print("Seven swans a swimming,")
                case 6:
                    print("Six geese a laying,")
                case 5:
                    print("Five golden rings,")
                case 4:
                    print("Four calling birds,")
                case 3:
                    print("Three french hens,")
                case 2:
                    print("Two turtle doves, and")
                case default:
                    print("a partridge in a pear tree.\n")
            day -= 1
    else:
        print("There is no", day, "day of Christmas. Input between 1 and 12")


if __name__ == '__main__':
    days_of_xmas = int(input("Enter day of Christmas\nor press 0 to quit\n"))
    while days_of_xmas > 0:
        christmas_song(days_of_xmas)
        days_of_xmas = int(input())
