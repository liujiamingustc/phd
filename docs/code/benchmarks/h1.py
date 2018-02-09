import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LogNorm
from mpl_toolkits.mplot3d import Axes3D

try:
    import numpy as np
except:
    exit()

from surrogate import benchmarks


def h1_arg0(sol):
    return benchmarks.h1(sol)[0]


fig = plt.figure()
# ax = Axes3D(fig, azim = -29, elev = 50)
ax = Axes3D(fig)
X = np.arange(-25, 25, 0.5)
Y = np.arange(-25, 25, 0.5)
X, Y = np.meshgrid(X, Y)
Z = np.fromiter(map(h1_arg0, zip(X.flat, Y.flat)), dtype=np.float, count=X.shape[0] * X.shape[1]).reshape(X.shape)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, norm=LogNorm(), cmap=cm.jet, linewidth=0.2)

plt.xlabel("x")
plt.ylabel("y")

plt.show()