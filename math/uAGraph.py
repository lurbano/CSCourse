import matplotlib.pyplot as plt


class uAGraph:
    def __init__(self, xmin=0, xmax=10, xLabel="x", yLabel="y"):
        self.x = []          
        self.y = []
        self.fig, self.ax = plt.subplots()    # initialize matplotlib plot
        plt.xlim([xmin, xmax])
        self.ax.set_xlabel(xLabel)  # label axes
        self.ax.set_ylabel(yLabel)  # label axes
        self.ax.plot(self.x, self.y)               # put data into plot (line)
        self.ax.scatter(self.x, self.y)        

    def add(self, x, y):
        self.x.append(x)
        self.y.append(y) 
        self.ax.plot(self.x, self.y)               # put data into plot
        self.ax.scatter(self.x, self.y)

    def wait(self, dt):
        plt.pause(dt)