from textInator import * 

files = ["45.txt", "46.txt"]
#files = ["45OctMN.txt", "46OctNV.txt"]

fig, ax = plt.subplots()
#t = textInator("46OctNV.txt")
#t = textInator("45OctMN.txt")
for file in files:
    t = textInator(file)
    nwords = t.wordCount()
    nchars = t.charCount()
    print(f"Stats: {file}")
    print(f"   Words: {nwords}")
    print(f"   Char: {nchars}")
    print(f"   chars/words: {nchars/nwords}")
    print(f"   Unique Words: {len(t.uniqueWords)}")
    print(f"   Unique/Total: {len(t.uniqueWords)/nwords}")
    t.wordFrequency()
    (x, y) = t.wordLengths()


    ax.plot(x, y, label=file)

plt.legend(loc="upper left")
plt.show()
