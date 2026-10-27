
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(data, bins=10, color='green'):
    mean = np.mean(data)
    std = np.std(data)

    plt.hist(data, bins=bins, color=color)
    plt.axvline(mean, color='red')

    plt.title('Standard Deviation = ' + str(std))
    plt.xlabel('Values')
    plt.ylabel('Frequency')

    plt.show()

data = [np.random.normal(50, 10, 100)]

plot_histogram(data)
