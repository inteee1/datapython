import matplotlib.pyplot as plt
import numpy as np
# data = [1,2,3,4,]
# plt.plot(data)
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.show()

# x = [i for i in np.linspace(0, 10, 1_000)]
# y = [i **2 for i in x]
# print(y)
# plt.plot(x, y, 'o')
# plt.show()
x = np.arange(-20, 20) # -20에서 20사이의 수를 1의 간격으로 생성
y1 = 2 * x # 2* x를 원소로 가지는 y1 함수
y2 = (1/3) * x ** 2 + 5 # -x**2 + 5 를 원소로 가지는 y2함수
y3 = -x ** 2 - 5 # -x**2-5를 원소로 가지는 y3 함수
#빨강색 점선, 녹색 실선과 세모기호, 파랑색 별표와 점선으로 함수를 표현

plt.plot(x, y1, 'g--', x, y2, 'r^-', x, y3, 'bv:')
plt.axis([-30, 30, -30, 30]) #그림을 그릴 영역을 지정함
plt.show()