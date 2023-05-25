import numpy as np
from math import sin
data = np.linspace(0, np.pi, 11)
result = list()
for i in data:
    result.append(sin(i))
    pass
print(result)