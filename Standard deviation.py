import pandas
x = []
d = []
dsq = []
clear = []

N = int(input("Enter the number of terms(Frequncy) "))

# input 
for i in range(0, N):
    x_temp = int(input("Enter the number "))
    x.append(x_temp)

# mean 
mean = sum(x)/N
mean = int(mean)

# d
for i in range(N):
    d_temp = x[i]- mean
    d.append(d_temp)

# d square
for i in range(N):
    dsq_temp = d[i] * d[i]
    dsq.append(dsq_temp)

sum_dsq = sum(dsq)
dsq.append(sum_dsq)

x.append(clear)
d.append(clear)

# printing mechanism
data = {
    "  X   ": x,
    "  d   ": d,
    "  d^2 ": dsq
}

standevi = (sum_dsq/N)(1/2)
df =pandas.DataFrame(data)
print(df)
print(standevi)