from cmath import sin
import matplotlib.pyplot as plt

x = []
y = []

for i in range(11):
    f = sin(i)
    #print(x, f)
    x.append(i)
    y.append(f)     # add to array

print(y)

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()