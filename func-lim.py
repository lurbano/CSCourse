import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
    y = (x**2 - 2*x)/(x-2)
    return y 

x = []
y = []

for i in range(-5, 5):
    try: 
        y.append(f(i))
        x.append(i)
        print(x[-1], y[-1])
    except:
        a = 1


fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()