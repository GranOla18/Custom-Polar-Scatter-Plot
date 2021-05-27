import numpy as np
import matplotlib.pyplot as plt


# Fixing random state for reproducibility
#np.random.seed(19680801)

# Compute areas and colors
N = 1
r = [4, 3]
theta = [2, 6] 
area = 200
colors = theta

fig = plt.figure(dpi = 100)
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)