import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
    return 0.5*x+3

def get_mean(a): # a is an array
    n = 0
    tot = 0
    for x in a:
        tot += x 
        n += 1 
    avg = tot / n
    return avg


n = 11
x = [0,1,2,3,4,5,6,7,8,9,10]
y = [2.8,3.6,4.0,4.4,5.0,5.8,6.2,6.1,7.4,7.2,8.2]

y2 = []
for i in x:
    y2.append(f(i))
print(y2)

sum_diff = 0
sum_diff_sq = 0

sum_squares = 0

# deviations
for i in range(n):
    xval = x[i]

    # difference (residuial)
    d = y[i] - f(xval)
    d_sq = d**2

    #add sums
    sum_diff += d 
    sum_diff_sq += d_sq

    # sum of the squares
    d = y[i] - get_mean(y)
    sum_squares += d**2

r_squared = 1 - sum_diff_sq / sum_squares

print(f"Sum of differences = {sum_diff}")
print(f"Sum of differences squared = {sum_diff_sq}")
print(f'r^2 = {r_squared}')




fig, ax = plt.subplots()
ax.scatter(x, y)
ax.plot(x,y2)

plt.show()
