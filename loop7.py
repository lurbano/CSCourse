import numpy as np
import matplotlib.pyplot as plt

x = []
y = []

for i in range(21):
    f = i**2-3*i+4
    #print(x, f)
    x.append(i)
    y.append(f)     # add to array

print(y)

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()