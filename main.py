#rock-paper-scissors project
""" 
steps:
import random
- create a list to store all possible options ["R", "P", "S"]
- loop game till a certain condition is met to terminate the game
- receive players input and validate players input with our defined list
- cpu play is made using the random.choice method
- print both plays options
- check and compare both play moves
- select a winner if both play moves are not the same
- restart game if both play moves are the same

"""
import random

print("WELCOME TO THE GAME OF ROCK, SCISSORS AND PAPER \n\n")

is_running = True
game_list = ["R", "P", "S"]
game_list_dict = { "R": "Rock", "P":"Paper", "S":"Scissors"}

while(is_running):
    player1 = input("please select a move from the following: R: rock, P: paper, S: scissors \n")
    upPlayer1 = player1.upper()
    if upPlayer1 in game_list:
        player_cpu = random.choice(game_list)
        if upPlayer1 != player_cpu:
            if upPlayer1 == "R" and player_cpu == "P" :
                print("Player(Rock) : CPU(Paper)\n")
                print("you lost unfortunately, Paper wins")
            if upPlayer1 == "R" and player_cpu == "S" :
                print("Player(Rock) : CPU(Scissors)\n")
                print("you WIN!, Rock wins")
            if upPlayer1 == "P" and player_cpu == "R" :
                print("Player(Paper) : CPU(Rock)\n")
                print("you WIN!, Paper wins")
            if upPlayer1 == "P" and player_cpu == "S" :
                print("Player(Paper) : CPU(Scissors)\n")
                print("you lost unfortunately, Scissors wins")
            if upPlayer1 == "S" and player_cpu == "P" :
                print("Player(Scissors) : CPU(Paper)\n")
                print("you WIN!, Scissors wins")
            if upPlayer1 == "S" and player_cpu == "R" :
                print("Player(Scissors) : CPU(Rock)\n")
                print("you lost unfortunately, Rock wins")
            is_running = False
        else:
            
            print("Player(" + game_list_dict[upPlayer1] + ") : CPU(" + game_list_dict[player_cpu] + ")")
            print("it is a TIE!\nTry again")