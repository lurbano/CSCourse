# fibonacci

n = 30      # number of members

# initialization
f1 = 1
f2 = 1

print(f1)
print(f2)

for i in range(2, n+1):

    # calculations
    f_new = f1 +  f2
    print(f_new)

    #update
    f1 = f2 
    f2 = f_new