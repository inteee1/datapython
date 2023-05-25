import numpy as np
b = np.array([[1, 1], [2, 2], [3, 3]])
c = np.insert(b, 1, 4, axis =0)
print(c)

d = [1, 3, 4]
d.insert(1,2)
print(d)

e = np.array([[1, 2, 3, ], [4, 5, 6]])
e = np.flip(e, axis = 1)
print(e)

f = np.array([10,20,30])
f_max = f.max()
f_min = f.min()
f_mean = f.mean()
f_astype = f.astype(np.float64)
print(f_max, f_min, f_mean, f_astype)

g = np.array([[1,1], [2,2], [3,3]])
print(g.flatten())
print(g.T)

h = np.array([3, 5, 8, 1, 0])
h.sort()
print(h)

i = np.array([[35, 24, 55], [69, 19, 9], [4, 1, 11]])
i.sort()
print(i)

j = np.array([[35, 24, 55], [69, 19, 9], [4, 1, 11]])
j.sort(axis=0)
print(j)

k = np.array([[35, 24, 55], [69, 19, 9], [4, 1, 11]])
k_1 = np.flip(k, axis = 1)
k_2 = np.flip(k, axis = 0)
print(k_1)