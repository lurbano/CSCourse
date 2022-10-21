with open("testFile.txt") as f:
    lines  = f.readlines()

print(lines)

newlines = []
for line in lines:
    print(line)

    if (line.find("Page") != 0):
            newlines.append(line)

print(newlines)