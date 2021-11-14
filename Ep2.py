import numpy as np
import matplotlib.pyplot as plt


def moving_average(a, n=10):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


with open("signal01.dat", "r") as file:
    data_y = np.array([float(x) for x in file.read().split()])

plt.grid(True)
data_x = np.linspace(0, 100, data_y.size)
data_y_new = moving_average(data_y)
plt.title("Сырой сигнал")
plt.plot(data_x, data_y)
plt.show()
plt.gcf()
plt.grid(True)
data_x = np.linspace(0, 100, data_y.size - 9)
plt.title("После фильтрации")
plt.plot(data_x, data_y_new)
plt.show()
