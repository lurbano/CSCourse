from textInator import *

tFile = textInator("reflections.txt")
tFile.getSentences()

for s in tFile.sentences:
    print(s)
print("number of sentences:", len(tFile.sentences))

w = "who"
print(f"Number of '{w}': {tFile.countWord(w)}")

# print("Number of lines:", tFile.fileLength())



# with open("reflections.txt") as f:
#     fullText = f.read()

# fullText = fullText.replace('\n', ' ')
# sentences = fullText.split(".")

# for s in sentences:
#     print("*: ", s)



# print(tFile.nSentences())

# print("Number of sentences:", len(tFile.sentences))
