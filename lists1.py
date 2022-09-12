costs = [10.00,18.00,18.00,11.00,17.50,11.00,17.50,11.00,17.50,11.00,30.00,17.50,20.50,11.50,6.50,5.60,7.50 ]

total = 0 

for i in costs:
    total = total + i
    print(i, total)

avg = total / len(costs)
print("Average Cost = ", avg)