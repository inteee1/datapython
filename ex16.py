import matplotlib.pyplot as plt
import numpy as np


f1 = np.random.normal(loc=0, scale=1, size=10000)
f2 = np.random.normal(loc=3, scale=0.5, size=10000)

plt.hist(f1, bins=200, color='red', alpha=0.7, label='loc = 0, scale = 1')
plt.hist(f2, bins=200, color='blue', alpha=0.5, label='loc = 3, scale = 0.5')
plt.show()