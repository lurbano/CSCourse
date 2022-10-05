
def lineCount(filename):
    '''Counts the number of lines in a file'''
    with open(filename) as f:
        lines = f.readlines()
    return len(lines)


with open('terence.txt') as f:
    lines = f.readlines()

    
# print(lines)
print("Length: ", lineCount('terence.txt'))
    
print(lines[0])
print(lines[0][0])
print(lines[0][-2])
print(len(lines[0]))

l1 = lines[0].strip().split(" ")
print(l1, len(l1))

# write a program to:
## go through each line in the array and print out the number of words in each line.
## 