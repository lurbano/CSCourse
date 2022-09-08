n = 25699
isPrime = True

for i in range(2, n):
    #print(n, i, n%i)
    if n%i == 0:
        print("Not a prime")
        isPrime = False
        break

if isPrime == True:
    print("Is a prime.")
    


