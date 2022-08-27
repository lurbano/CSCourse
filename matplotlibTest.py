import numpy as np
import matplotlib.pyplot as plt

r = .09
N = 1000
dt = 1
 

xa = []
ya = []

for d in range (51):
    xa.append(d)   #Days
    ya.append(N)   #Cases
    dN = r * N * dt    #change in cases
    N = N + dN
print(d, N)

    

fig, ax = plt.subplots()
ax.plot(xa, ya)

plt.show()