for i in range(2, 101): 
    a = 0
    for j in range(1, i + 1):
        if i % j == 0:
            a += 1
    if a == 2:  
        print(i, end=' ')
