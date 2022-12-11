def grade_book():
    score = int(input("Input score\n"))
    i = 0
    while i < 3:
        if i != 0:
            score = int(input("\nInput score\n"))
        i += 1
        if score < 0 or score > 100:
            print("Invalid score")
        else:
            if score <= 39:
                print("Olodo osi")
            elif score <= 49:
                print("You no try - E")
            elif score <= 59:
                print("E remain small - D")
            elif score <= 70:
                print("You dey try - C")
            elif score <= 80:
                print("OG! - B")
            elif score <= 100:
                print("Agba! - A")


if __name__ == '__main__':
    grade_book()
