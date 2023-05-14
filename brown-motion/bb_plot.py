import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


N = 10000     
D = 1e-6     
dt = 0.01    
sigma = np.sqrt(2*D*dt)


x, y, z = 0, 0, 0


dx, dy, dz = sigma*np.random.randn(3, N)
x, y, z = np.cumsum(dx), np.cumsum(dy), np.cumsum(dz)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
