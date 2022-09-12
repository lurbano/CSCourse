costs = [10.00,18.00,18.00,11.00,17.50,11.00,17.50,11.00,17.50,11.00,30.00,17.50,20.50,11.50,6.50,5.60,7.50 ]

total = 0 

for i in costs:
    total = total + i
    print(i, total)

avg = total / len(costs)

totDev = 0

for i in costs:
    dev = (i - avg)**2
    totDev = totDev + dev

sd = (totDev/len(costs))**0.5
print(f"stdev = {sd}")