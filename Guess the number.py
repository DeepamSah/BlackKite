import random
x = random.randint(1, 100)

option = 15


while option > 0:
    y = int(input("Enter your guess "))
    option -= 1

    if x == y:
        print("^^^^^^^ You guessed the number in ", option ," tries ^^^^^^^")
        break
    elif y > x:
        print('^ Too high ^')   
        print("-_- You guessed the wrong number. You have ", option ," tries left -_-")

    elif x > y:
        print("_ Too low _")   
        print("-_- You guessed the wrong number. You have ", option ," tries left -_-")

 
if option == 0:
    print("You failed miserably ")
