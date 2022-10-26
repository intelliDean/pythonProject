def nested_if(sport, p1_score, p2_score):
    if p1_score == p2_score:
        print("The game is a draw.")
    elif sport.lower() == "basketball":
        if p1_score > p2_score:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
    elif sport.lower() == "golf":
        if p1_score < p2_score:
            print("Player 2 wins")
        else:
            print("Player 1 wins")
    else:
        print("Unknown sport")


if __name__ == '__main__':
    print(nested_if("golf", 45, 54))
