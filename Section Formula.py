print("Ratio is m:n")
x1 = int(input("Enter the coordinate of x1 "))
y1 = int(input("Enter the coordinate of y1 "))
x2 = int(input("Enter the coordinate of x2 "))
y2 = int(input("Enter the coordinate of y2 "))

m = int(input("Enter the ratio m "))
n = int(input("Enter the ratio n "))
opt= int(input("Enter one for internal section and 2 for external section "))
extx = (m*x2-n*x1)/(m-n)
exty = (m*y2-n*y1)/(m-n) 
intx = (m*x2+n*x1)/(m+n)
inty = (m*y2+n*y1)/(m+n)
if opt == 1:
    print("The point on the line is (",intx,",",inty,")" )
elif opt == 2:
    
    print("The external point is (",extx,",",exty,")")
else:
    print("_____")