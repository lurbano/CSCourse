size = input("What size would you like? ")

size = size.lower().strip().replace(' ', "")


if size == 'venti':
    print("You probably should have something smaller.")
elif size == 'tall':
    print("Do you mean small?")
elif size == "grande":
    print("Now nice.")
else:
    print("What are you talking about?")

