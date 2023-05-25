import numpy as np

a = np.arange(10, 18).reshape(2,4)
b = np.arange(12).reshape(3,4)
c = np.arange(8).reshape(2,4)
d = list(range(4))
print(a) #(2,4) 형상의 다차원 배열로 10에서 17까지의 원소를 가짐
print(b) #(3,4) 형상의 다차원 배열로 0에서 11까지의 원소를 가짐
print(c) #(2,4) 형상의 다차원 배열로 0에서 7까지의 원소를 가짐
print(d) #1차원 리스트로 0에서 3까지의 원소를 가짐
print(np.concatenate((a,b))) #a 배열의 마지막 원소 다음에 B배열을 넣는다
print(np.vstack((a,b))) #a 배열과 B 배열을 수직뱡향으로 결합
print(np.vstack((a, d)))
print(np.vstack((a, b, d)))
print(np.hstack((a, c))) # a배열과 C를 수평으로 결합
#print(np.hsatack(a,b)) # a배열과 b배열의 hsatck 결합-오류, a 배열은 형상이(2,4), b배열은 (3,4)

e = np.array([1,2,3])
f = np.array([10, 20, 30])
g = np.array([[1,2,3], [4,5,6]])
h = np.array([[10, 20, 30], [40, 50, 60]])
print(np.r_[e,f])
print(np.r_[e, 4, 5, 6, f])
print(np.r_[[0] * 3, 5, 6])
print(np.r_[g, h])
print(np.r_[e.reshape(-1, 1), f.reshape(-1,1)])