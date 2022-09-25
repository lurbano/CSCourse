#Functions 
def f(x):
    y = (x**2)/4
    return y 

x = []
y = []

for i in range(0, 11):
    x.append(i)
    y.append( f(i) )

print("x: ", x)
print("y: ", y)