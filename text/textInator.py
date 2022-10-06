class textInator:
    '''Analyze texts using stats and such.'''

    def __init__(self, filename):
        self.fname = filename
        with open(self.fname) as f:
            self.lines = f.readlines()

    def fileLength(self):
        n = len(self.lines)
        return(n)

