import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '2.5',c = 'hotpink',ls = ':')
plt.savefig("p2.png")
