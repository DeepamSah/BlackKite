a = int(input('Enter any number'))
b = a 
re = 0 

while a != 0:
    r = a % 10 
    re = re *10 +r 
    a = a//10

print('The reverse of the number is ', re) 
if re == b:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")