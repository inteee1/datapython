import numpy as np

def train_test_split(data:list) -> tuple:
    size = int(len(data) * 0.8)
    train_data = data [:size]
    test_data = data[size:]
    return (train_data, test_data)

data = np.arange(1, 51)
np.random.shuffle(data)
print(data)
print(train_test_split(data))

np_array = np.array([[1,2,3,4], [5,6,7,8],[9,10,11,12],[13,14,15,16]])
np_array % 2== 0
print(np_array % 2== 0)
print(np_array[np_array % 2== 0])

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9],[0,1,2]])

print(arr_2d[1: , 0:3])

a = np.array([[1,2], [1, -3]])
b = np.array([6, 1])
s = np.linalg.solve(a, b)
print(s)
                
A = np.array([[1,1,-1], [2, -1, 3], [1, 2, 1]])
#det_A = np.linalg.det(A)
B = np.array([0, 9, 8])
#det_B = np.linalg.det(B)
S = np.linalg.solve(A, B)
print(S)



