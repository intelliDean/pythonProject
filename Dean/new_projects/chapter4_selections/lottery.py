import random


def lottery_game(guess):
    lottery = random.randint(10, 99)

    # Get digits from lottery
    lottery_digit1 = lottery // 10
    lottery_digit2 = lottery % 10

    # Get digits from guess
    guess_digit1 = guess // 10
    guess_digit2 = guess % 10

    print("The lottery number is", lottery)

    # Check the guess
    if guess == lottery:
        print("Exact match: you win $10,000")
    elif guess_digit2 == lottery_digit1 and guess_digit1 == lottery_digit2:
        print("Match all digits: you win $3,000")
    elif guess_digit1 == lottery_digit1 or guess_digit1 == lottery_digit2 \
            or guess_digit2 == lottery_digit1 or guess_digit2 == lottery_digit2:
        print("Match one digit: you win $1,000")
    else:
        print("Sorry, no match")


if __name__ == '__main__':
    lottery_game(eval(input("Enter two digits number for your lottery pick\n")))
