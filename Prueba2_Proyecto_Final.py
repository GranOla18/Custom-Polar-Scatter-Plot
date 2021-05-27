import numpy as np
import matplotlib.pyplot as plt


# Fixing random state for reproducibility
#p.random.seed(19680801)

# Compute areas and colors
"""
N = 150
r = 2 * np.random.rand(10)
print(r)
theta = 2 * np.pi * np.random.rand(10)
area = 200 * r**2
colors = theta
print(colors)

fig = plt.figure(facecolor = "lightcyan", figsize = [4, 4], dpi = 200, linewidth = 20, edgecolor = "Pink")
ax = fig.add_subplot(111, projection='polar')
#111 = posición, default pone 111
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

#x = pi/2, etc // y = nivel en el que está
"""

#r  //  y
lArr = [1,2,3,4,5]
cosa = np.pi * np.random.rand(6)
#theta  //  x
cosa2 = np.array([7, 3.5, 5.3, 3.1, 4.9])
#Este número son grados
#De grados a radianes = grados * 180 / pi

#theta
lArr3 = 2 * cosa
areaa = 2000
#area de las bolitas
colores = np.random.rand(5)
print(colores)

fig = plt.figure(dpi = 150)
axx = fig.add_subplot(projection = 'polar')
d = axx.scatter(cosa2, lArr, c = colores, s = areaa, cmap = 'hsv', alpha = 0.75)

plt.savefig('d.png')

y_2 = np.random.uniform(1, 4, size = 4)
print(y_2)
print(type(y_2))