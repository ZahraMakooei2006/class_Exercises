
import matplotlib.pyplot as plt

def plot_line(x, y, title):
    plt.plot(x, y, color='red', linestyle='--')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 6, 5]

plot_line(x, y, 'My Line Plot')
