import random

# Game function
def roll():
    roll=random.randint(1,6)

    return roll


# Introduction to the game
print("Welcome To Pig Game")
print("\t^-^")

# Ask no of players and store.
while True:
    players=input("Enter number of players(2-4): ")
    if players.isdigit() and int(players) in range(2,5):
        players=int(players)
        break
    else:
        print("Invalid!Try Again")

# Define the scores
max_score=50
player_score=[0 for _ in range(players)]
print("Starting The Round...")

# Play game until max score is reached 
# Checks after every iteration of the players list
while max(player_score) < max_score:
    for player_idx in range(players):
        current_score=0
        print("*"*3+"Player "+str((player_idx+1))+"*"*3)
        print(f"Your standing score is: {player_score[player_idx]}\n")

        while True:
        #   While loop for each players turn
            should_roll=input("Would you like to play(y)?: ")
            if should_roll.lower() != "y":
                break

            else:
                value=roll()
                if value ==1:
                    current_score=0
                    player_score[player_idx]=0
                    print("You Rolled a 1!Turn Done!")
                    break

            current_score = current_score + value
            print(f"You rolled a {value}!Your current score is {player_score[player_idx]+current_score}!")
        
        player_score[player_idx]+=current_score
        print(f"Your Total score is {player_score[player_idx]}\n")

# loop break after max score is reached 
max_score=max(player_score)   
winning_index=player_score.index(max_score)
print(f"\n player {winning_index + 1} won with a score of {max_score}") 
print("\t*(^o^)*")