import numpy as np 
import matplotlib.pyplot as plt 

def slope(x1, y1, x2, y2):
    dx = x2-x1 
    dy = y2-y1
    try:
        m = dy/dx 
    except:
        m = None
    return m

def yint(x1,y1,x2,y2):
    b = -slope(x1,y1,x2,y2) * x2 + y2
    return b

s = slope(2,5, 4,10)
print(s)
b = yint(2,5,4,10)

x, y = [], []

for i in range(-10, 11):
    x.append(i)
    y.append(s*i+b)

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()

