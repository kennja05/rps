from random import randint

plays = ["rock", "paper", "scissors"]
computer = plays[randint(0,2)]
player = False
wonMatch = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

while not player:
    
    player = input("Rock, Paper, or Scissors?\n").lower()
    
    #check for valid entry
    while player not in plays:
        player = False
        print("Invalid entry. Try again")
        player = input("Rock, Paper, or Scissors?\n").lower()
    
    #check for tie and use wonMatch dict if winner
    if player == computer:
        print("Tie!")
    elif wonMatch[player] == computer:
        print("You Win!") 
    else:
        print("You lose!")
    
    #option to loop through and play again
    playAgain = input("Play again? y/n: ")
    if playAgain == 'y':
        player = False
        computer = plays[randint(0,2)]
    else:
        print("Game Over")