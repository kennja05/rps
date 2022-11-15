from random import randint

plays = ["rock", "paper", "scissors"]

computer = plays[randint(0,2)]
player = False
wonMatchup = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
while not player:
    player = input("Rock, Paper, or Scissors?\n").lower()
    if player == computer:
        print("Tie!")
    elif wonMatchup[player] == computer:
        print("You Win") 
    elif wonMatchup[computer] == player:
        print("You lose")
    else:
        print("Invalid entry")
player = False
computer = plays[randint(0,2)]