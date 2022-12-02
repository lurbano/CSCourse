import numpy as np
from ezGraph import *

# initial values

G = 20

dt = 1

graph = ezGraph()

for t in range(0, 10, dt):
    dG = 0.5 * t * dt
    G = G + dG
    print(t, G)
    graph.add(t, G)

graph.keepOpen()