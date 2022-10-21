import numpy as np
import matplotlib.pyplot as plt

class textInator:
    '''Analyze texts using stats and such.'''

    def __init__(self, filename):
        self.fname = filename
        with open(self.fname) as f:
            self.lines = f.readlines()
        with open(self.fname) as f:
            self.fullText = f.read()
            self.fullText = self.fullText.replace('\n', ' ')
        self.getWords()
        

    def fileLength(self):
        n = 0
        for line in self.lines:
            line = line.strip()
            print(line, len(line))
            if line != '':
                n = n + 1
        return(n)

    def getSentences(self):
        fullText = self.fullText.replace('\n', ' ')
        self.sentences = fullText.split(".")

    def countWord(self, word):
        n = 0
        for s in self.sentences:
            if word in s:
                n += 1
        return n

    def removePunct(self):
        removables = ['.', ',', '"', "'", '“', '-', '...', '?', ":", "’", '…']
        fullText = self.fullText.replace(".", " ")
        for r in removables:
            fullText = fullText.replace(r, " ")
        return fullText

    def getWords(self):
        words = self.removePunct().split()
        self.words = []
        for w in words:
            if len(w) > 0:
                self.words.append(w.lower())
        self.uniqueWords = set(self.words)
        return (self.words)
        
    def wordCount(self):
        return len(self.words)

    def getChars(self):
        charString = self.removePunct().replace(" ", "")
        return charString

    def charCount(self):
        return len(self.getChars())

    def wordFrequency(self):
        wordFreq = {}
        for u in self.uniqueWords:
            wordFreq[u] = 0
            for w in self.words:
                if u.lower() == w.lower():
                    wordFreq[u] += 1
        self.sortedWords = {}
        sortedKeys = sorted(wordFreq, key=wordFreq.get)
        for w in sortedKeys:
            self.sortedWords[w] = wordFreq[w]
        #print(self.sortedWords)
        return(self.sortedWords)

    def wordLengths(self, n=1):
        wordLengthList = []
        for i in range(30):
            wordLengthList.append([])
        for w in self.uniqueWords:
            n = len(w)
            wordLengthList[n].append(w)

        x, y = [], []
        n = 0
        for i in wordLengthList:
            x.append(n)
            y.append(len(i))
            n = n+1

        # #print(wordLengthList)
        # for i in range(9, 20):
        #     print(i, len(wordLengthList[i]), wordLengthList[i])

        return (x, y)

        









    # def nSentences(self):
    #     with open(self.fname) as f:
    #         txt = f.read()

    #     # remove newlines 
    #     txt = txt.replace('\n', '')
    #     self.sentences = txt.split(".")
    #     print(self.sentences)     


