import random
x = int(input("Enter the number limit of the password "))
a = ""
characters = "qwertyuioplkjhgfdsazxcvbnm@#%1234567890"

for i in range(1, x+1):
    opt = random.choice(characters)
    a = a+opt

print(a)