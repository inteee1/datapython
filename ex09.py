import numpy as np

a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])
#print([a].append(b, axis=0))

c = np.arange(12)
print(c)
print(c.reshape(-1, 4))

#평균값이 165, 표준편차가 10인값 생성
rnd = np.random.randn(5) * 10 + 165
print(rnd)

nums = np.random.normal(loc=165, scale=10, size=(3,4)).round(2)
print(nums)

a = np.arange(10) # 0,1 2, 3, 4, 5, 6, 7, 8  ,9 값을 생성
np.random.shuffle(a) #a에는 순서가 뒤섞인 값이 들어있다.
print(a)
b = np.random.permutation([2,4,6,8,10])
print(b)

data = np.arange(1, 51)
np.random.shuffle(data)
train_data = data[:int(0.8 * len(data))]
test_data = data[int(0.8 * len(data)):]
print(train_data)
print(test_data)

