import random

ch= ("Scissors", "Rock", "Paper")
computer = random.choice(ch)
option = 10
win = 0

while option > 0:
    human = input("Enter your choice ")
    if human == computer:
        print("Tie!!")
        option=-1 

    
    elif computer == "Paper":
        if human == "Scissors":
            print("^^^^^ You win ^^^^^")
            win=+1
            option=-1 
        else:
            print("_____ Your lose ______")
            option=-1 


    elif computer == "rock":
        if human == "Paper":
            print("^^^^^ You win ^^^^^")
            option=-1 
            win=+1
        else:
           print("_____ Your lose ______")
           option=-1 


    elif computer == "Scissors":
        if human == "Rock":
              print("^^^^^ You win ^^^^^")
              option=-1 
              win=+1
        else:
             print("_____ Your lose ______")
             option=-1 
    if win == 10:
        print("You won")