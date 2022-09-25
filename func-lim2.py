import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
    try:
        y = (x**2 - 2*x)/(x-2)
    except: 
        y = (f(x+dx) + f(x-dx)) / 2
    return y 

def limf(x):
    y = x
    return y

x = 2
dx = 1/1000000000

for i in range(-5,5):
    print(i, f(i))

