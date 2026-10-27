
import matplotlib.pyplot as plt

class BaseChart:
    def show(self):
        plt.show()

class BarChart(BaseChart):
    def __init__(self, categories, values):
        self.categories = categories
        self.values = values

    def plot(self):
        plt.bar(self.categories, self.values)

categories = ['Python', 'Java', 'C++', 'JavaScript']
values = [80, 60, 70, 90]

chart = BarChart(categories, values)

chart.plot()
chart.show()
