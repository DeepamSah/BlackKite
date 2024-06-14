

num = int(input('Enter the number of elements: '))
df = {
    '10-20':[],
    '20-30':[],
    '30-40':[], 
    '40-50':[], 
    '50-60':[], 
    '60-70':[], 
    '70-80':[],
    '80-90':[], 
    '90-100':[],
}

for i in range(0, num):
    x = int(input('Enter the element: '))
    if x in range(10, 20):
        df['10-20'].append(x)
    elif x in range(20, 30):
        df['20-30'].append(x)
    elif x in range(30, 40):
        df['30-40'].append(x)
    elif x in range(40, 50):
        df['40-50'].append(x)
    elif x in range(50, 60):
        df['50-60'].append(x)
    elif x in range(60, 70):
        df['60-70'].append(x)
    elif x in range(70, 80):
        df['70-80'].append(x)
    elif x in range(80, 90):
        df['80-90'].append(x)
    elif x in range(90, 100):
        df['90-100'].append(x)
 
print(df)
for i in range(0, 9):
    print(df[i][len])