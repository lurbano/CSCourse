import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
    dx = 0.0000000001
    try:
        y = (x**3 - 2*x)/(x-2)
    except: 
        y = (f(x+dx) + f(x-dx)) / 2
    return y 

x = []
y = []

for i in range(-5,5):
    x.append(i)
    y.append(f(i))
    print(i, f(i))

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()

