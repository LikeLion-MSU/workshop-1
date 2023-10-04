import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper" , "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)
    
    # your code goes here