from random import random

def coinFlip():
    A = random()
    result = ""
    if (round(A) == 1):
        result = "heads"
    else:
        result = "tails"
    return result

nHeads = 0
nTails = 0

nFlips = 2500000

for i in range(nFlips):
    if coinFlip() == "heads":
        nHeads = nHeads + 1
    else:
        nTails = nTails + 1 

print("Heads = ", nHeads, nHeads/nFlips)
print("Tails = ", nTails, nTails/nFlips)

    

