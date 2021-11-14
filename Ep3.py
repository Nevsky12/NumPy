import time
import numpy as np
import matplotlib.pyplot as plt

I = np.eye(50)
A = np.zeros((50, 50), float)
np.fill_diagonal(A, 1)
A[0, -1] = -1.
for i in range(49):
    A[i + 1, i] = -1.
with open("start.dat.txt", 'r') as file:
    U = np.array([float(x) for x in file.read().split()])

data_x = np.linspace(0, 50)
for i in range(255):
    plt.ion()
    U = U @ (I - 0.5 * A)
    plt.clf()
    plt.axis([0, 50, 0, 10])
    plt.grid(True)
    plt.plot(data_x, U)
    plt.draw()
    plt.gcf().canvas.flush_events()
    time.sleep(0.05)
    plt.show()

plt.ioff()
