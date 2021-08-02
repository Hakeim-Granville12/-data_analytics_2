# #Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game.)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock


print("Welcome to our Rock-Paper-Scissors game ")
print("let's Play! Remember to play fair.")
play = True
while play:
    player_1 = input("Enter rock, paper, or scissors ? ")
    player_2 = input("Enter rock, paper, or scissors ? ")
    if player_1 == "rock":
        if player_2 == "rock":
            print("It's a tie")
    elif player_2 == "scissors":
        print("rock beats scissors, Congratulations Player 1 wins!")
    elif player_1 == "paper":
        print("rock beats paper, Congratulations Player 2 wins!")
    elif player_1 == "paper":
        if player_2 == "paper":
            print("It's a tie")
    elif player_1 == "scissors":
        print(" scissors beat paper, Congratulations Player 2 wins!")
    elif player_1 == "rock":
        print("rock beats paper, Congratulations Player 1 wins!")
    elif player_1 == "scissors":
        if player_2 == "scissors":
            print(" It's a tie")
    elif player_2 == "paper":
        print("scissors beats paper, Congratulations Player 1 wins!")
    elif player_2 == "rock":
        print(" rock beats scissors, Congratulations Player 2 wins!")
play_again = input("Would you like to start a new game? Yes or No? ")
if play_again == "Yes":
    play = True
else:
    play = False
