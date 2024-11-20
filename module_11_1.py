import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

"""Matplotlib — библиотека на языке программирования Python для визуализации данных двумерной и трёхмерной графикой. 
Она позволяет создавать разнообразные графики и диаграммы, которые помогают лучше понять и интерпретировать данные."""

"""NumPy — Позволяет работать с многомерными массивами и матрицами, а также выполнять высокоуровневые математические функции над ними."""


data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
Z = (1 - X / 2 + X ** 5 + Y ** 3) * np.exp(-X ** 2 - Y ** 2)

fig, axs = plt.subplots(2, 2, layout='constrained')
pc = axs[0, 0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[0, 0])
axs[0, 0].set_title('pcolormesh()')

co = axs[0, 1].contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
fig.colorbar(co, ax=axs[0, 1])
axs[0, 1].set_title('contourf()')

pc = axs[1, 0].imshow(Z ** 2 * 100, cmap='plasma', norm=LogNorm(vmin=0.01, vmax=100))
fig.colorbar(pc, ax=axs[1, 0], extend='both')
axs[1, 0].set_title('imshow() with LogNorm()')

pc = axs[1, 1].scatter(data1, data2, c=data3, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[1, 1], extend='both')
axs[1, 1].set_title('scatter()')

plt.show()
