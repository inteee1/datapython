import matplotlib.pyplot as plt
import numpy as np


#x = np.arange(3)
x = [0, 1, 2]
years = ['2010', '2011', '2012']
domestic = [6801, 7695, 8010]
foreign = [777, 1046, 1681]
new_x = [ i + 0.3 for i in x]

plt.bar(x, domestic, width=0.25)
plt.bar(new_x, foreign, width=0.25)
plt.xticks(x, years)
plt.show()

