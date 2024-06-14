from matplotlib import pyplot as plt

cox1 = int(input("Enter the coefficient of x: "))
coy1 = int(input("Enter the coefficient of y: "))
con1 = int(input("Enter the constant term: "))
cox2 = int(input("Enter the coefficient of x: "))
coy2 = int(input("Enter the coefficient of y: "))
con2 = int(input("Enter the constant term: "))

first_point1 = None
last_point1 = None
first_point2 = None
last_point2 = None

for i in range(-1000, 1200):  # Adjust the range as needed
    for j in range(-100, 120):  # Adjust the range as needed
        if (cox1*i + coy1*j + con1) == 0:
            if first_point1 is None:
                first_point1 = (i, j)
            last_point1 = (i, j)
for i in range(-1000, 1200):  # Adjust the range as needed
    for j in range(-100, 120):  # Adjust the range as needed
        if (cox2*i + coy2*j + con2) == 0:
            if first_point2 is None:
                first_point2 = (i, j)
            last_point2 = (i, j)

if first_point1 is not None:
    print("First Point: ({}, {})".format(first_point1[0], first_point1[1]))
    print("Last Point: ({}, {})".format(last_point1[0], last_point1[1]))
else:
    print("No points found on the line.")
if first_point2 is not None:
    print("First Point: ({}, {})".format(first_point2[0], first_point2[1]))
    print("Last Point: ({}, {})".format(last_point2[0], last_point2[1]))
else:
    print("No points found on the line.")

plt.plot([first_point1[0], last_point1[0]], [first_point1[1], last_point1[1]], color='r', linestyle='-', label=f'Line 1 (c={con1})')
plt.plot([first_point2[0], last_point2[0]], [first_point2[1], last_point2[1]], color='b', linestyle='-', label=f'Line 2 (c={con2})')



plt.title('Point Calculator')

plt.xlabel('X-axis')

plt.ylabel('Y-axis')

plt.show()