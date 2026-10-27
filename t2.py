
import matplotlib.pyplot as plt

class ScatterPlotter:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self, color='blue', size=30):
        plt.scatter(self.x, self.y, color=color, s=size)

    def add_labels(self, xlabel, ylabel, title):
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)

x = [1, 2, 3, 4, 5]
y = [5, 3, 6, 2, 7]

sp = ScatterPlotter(x, y)

sp.plot(color='red', size=50)
sp.add_labels('X Axis', 'Y Axis', 'Scatter Plot')

plt.grid(True)
plt.show()
