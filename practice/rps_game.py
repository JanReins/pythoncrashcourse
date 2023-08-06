import random, sys
print("ROCK, PAPER, SCISSOR")

wins = 0
losses =0
ties = 0

while True:
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))

    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        player_move = input()
        if player_move == 'q':
            sys.exit()
        if player_move =='r' or player_move == 'p' or player_move == 's':
            break
        print("Type one of r, p, s, or q")
    if player_move == "r":
        print ("ROCK vs ...")
    elif player_move == "p":
        print("PAPER vs...")
    elif player_move == "s":
        print("SCISSOR vs...")

    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = "r"
        print("ROCK")
    elif random_number == 2:
        computer_move = "p"
        print("PAPER")
    elif random_number == 3:
        computer_move = "s"
        print("SCISSOR")

    if player_move == computer_move:
        print("It is a tie")
        ties = ties + 1
    elif player_move == "r" and computer_move == "s":
        print("You win!")
        wins = wins + 1
    elif player_move == "p" and computer_move == "r":
        print("You win")
        losses = losses + 1
    elif player_move == "s" and computer_move == "p":
        print("You win!")
        wins = wins + 1
    elif player_move == "r" and computer_move == "p":
        print("You lose!")
        losses = losses + 1
    elif player_move == "p" and computer_move == "s":
        print("You lose!")
        losses = losses + 1
    elif player_move == "s" and computer_move == "r":
        print("You lose!")
        losses = losses + 1
