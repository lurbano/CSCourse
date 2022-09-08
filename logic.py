n = input("Enter your name:")

length = len(n)

print(length)

if length < 6:
    print(f"{n} your name is short.")
else:
    print(f"Your name is not short {n}. It has {len} letters.")