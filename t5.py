
import numpy as np
import matplotlib.pyplot as plt

def plot_boxplot(data, labels):
    plt.figure(figsize=(8, 6))

    plt.boxplot(
        data,
        tick_labels=labels,
        patch_artist=True,
        flierprops=dict(marker='o', markersize=8)
    )

    plt.title("Box Plot")
    plt.xlabel("Data")
    plt.ylabel("Values")
    plt.grid()

    plt.show()


data = [
    np.random.normal(50, 10, 100),
    np.random.laplace(60, 15, 100),
    np.random.exponential(70, 100)
]

labels = ['Data 1', 'Data 2', 'Data 3']

plot_boxplot(data, labels)
