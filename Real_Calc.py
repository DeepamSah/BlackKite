def oper2():
    def add(x, y):
        return x+y

    def sub(x, y):
        return x-y

    def div(x, y):
        return x/y

    def mul(x, y):
        return x*y

    opt = int(input("Enter 1, 2, 3 and 4 for Addition, Subtraction, Division and Multiplication respectively"))
    x = int(input("Enter the first number "))
    y = int(input("Enter the second number "))

    if opt == 1:
        print(add(x, y))
    elif opt == 2:
        print(sub(x, y))
    elif opt == 3:
        print(div(x, y))
    elif opt == 4:
        print(mul(x, y))
    else:
        print("The number entered is undesirerable")

def oper1():
    opt1 = int(input("Enter 1 for exponential calculation, 2 for square root calculation, 3 for cube root calculation, 4 for factorial calculation"))
    a = int(input("Enter the number "))
    if opt1 == 1:
        exponent = int(input("Enter the exponent of the number "))
        expon_print = a^exponent 
        print("The result is ", expon_print)
    elif opt1 == 2:
        squ_root = a^(1/2)
        print("The square root is ", squ_root)
    elif opt1 == 3:
        cube_root = a^(1/3)
        print("The cube root of the number is ", cube_root)
    elif opt1 == 4:
        b= 1
        for i in range(1,a+1):
            b = b *i 
        print("The factorial of the number is ", b)

print("Welcome to the Real Calculator ")
user = int(input("Enter 1, 2 for two-digit, single-digit calculation"))
if user == 1:
    oper2()
else:
    oper1()