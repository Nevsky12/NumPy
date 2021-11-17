import numpy as np
import matplotlib.pyplot as plt

with open("signal01.dat", "r") as file:
    data_y = np.array([float(el) for el in file.read().split()])

data_x = np.linspace(0, 100, data_y.size)
data_y_new = np.zeros(100)
sum_data = 0
step = 10

for i in range(data_y.size):
    if i + 1 <= step:
        data_y_new[i] = data_y[:i+1].mean()
    else:
        data_y_new[i] = data_y[i-10:i].mean()


plt.subplot(1, 2, 1)
plt.title("Сырой сигнал")
plt.grid(True)
plt.plot(data_x, data_y)

plt.subplot(1, 2, 2)
plt.title("После фильтра")
plt.grid(True)
plt.plot(data_x, data_y_new)
plt.show()

