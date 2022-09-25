def f1(x):
    return 2*x 

def f2(x, f):
    a = f(x)
    print(a) 

print(f1(3))
f2(4,f1)