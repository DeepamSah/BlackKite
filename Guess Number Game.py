import random
option = random.randint(1, 20)

gameleft = 15

while gameleft > 0:
    x = int(input("Enter the number to be guessed "))

    if x == option:
        print("Wow! you have guessed the number")
    else:
        print("You have guessed the wrong number ", gameleft-1, " guesses left")
    gameleft-=1
        
if gameleft == 0:
    print("You lose the game the number was ", option)
