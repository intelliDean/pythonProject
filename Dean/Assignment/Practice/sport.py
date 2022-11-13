def sport_game(sport, p1_score, p2_score):  # 1
    if sport.lower() == "basketball":
        if p1_score == p2_score:
            print("The game is a draw.")
        elif p1_score > p2_score:
            print("Player 1 wins.")
        else:
            print("Player 2 wins.")
    # 2
    elif sport.lower() == "golf":
        if p1_score == p2_score:
            print("The game is a draw.")
        elif p1_score < p2_score:
            print("Player 1 wins.")
        else:
            print("Player 2 wins.")
    # 3
    else:
        print("Unknown sport")


if __name__ == '__main__':
    sporty = input("Enter a sport\n")
    score1 = int(input("Enter player 1 score\n"))
    score2 = int(input("Enter player 2 score\n"))
    sport_game(sporty, score1, score2)
