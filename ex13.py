import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi * 2, 100) 
fig = plt.figure()
plt.plot(x, np.sin(x), 'r-', label='sin curve')
plt.plot(x, np.cos(x), 'b:', label='cos curve')
plt.xlabel('x value')
plt.ylabel('y value')
plt.legend(loc='best')

#fig.savefig('sin_cos_fig.png')
plt.show()

