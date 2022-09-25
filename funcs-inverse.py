
def f(x):
    return x**2 / 4

def g(x):
    return 2 * x**0.5 

print(f(2), g(9)) # check to see if functions are working

n = 3 
print("Starting value = ", n)
b = f(n)
print(f'f({n}) = {b}')

c = g(b)
print("g(b) =", c)

if n == c:
    print("Functions are inverse")
else:
    print("You failed.")
