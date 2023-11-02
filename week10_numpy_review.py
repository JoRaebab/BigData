import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
# linalg == linear algebra
np.random.seed()
a = np.random.uniform(size=10).reshape(2, 5) #균등 분포(일양 분포)
b = np.random.normal(0, 1, 100) #정규 분포
print(a)
print(b)
plt.hist(b)
plt.show()

# X = np.array([
#     [1, 2, 3],
#     [1, 0, 0],
#     [0, 0, 1]
# ])
# print(X)
# Z = inv(X)
# print(Z)
# print(X.dot(Z))

# a = np.arange(1, 7).reshape(2, 3)
# b = np.array([
#     [5, 20],
#     [11, -1],
#     [9, 3]
# ])
# print(a.dot(b))
# print(np.dot(a, b))
# print(b.dot(a))
# print(np.dot(b, a))



# a1 = np.arange(1, 6)
# a2 = np.array([6, 7, 8, 9, 10])
# a3 = np.array([
#     [3, 2, 1],
#     [-11, 0, 9]
# ])
# print(a1 + a2)
# print(a1 - a2)
# print(a1 * a2)
# print(a1 / a2)
# print(np.dot(a1, a2))
# # a3 = a1 + a2
# # print(a3)
# print(np.sum(a1) + np.sum(a2))
# print(np.prod(a1), np.prod(a2))
# # by aixs
# print(a3.sum(axis=0))
# print(a3.sum(axis=1))
# print(a3.prod(axis=0))
# print(a3.prod(axis=1))
# print(a3.mean()) # 산술 평균
# print(a3.std()) # 표준 편차


# a1 = np.ones((3, 3))
# a1[:, 2] = 2
# print(a1)
# a2 = np.full((3, 3), 5)
# print(a2)
# a3 = np.eye(3) # 단위 행렬
# print(a3)
# a4 = a3[:2, 1:]
# print(a4)
# a5 = a3[2]
# print(a5)
# a6 = a3[1, :2]
# print(a6)
# a7 = a3[:, :2]
# print(a7)

# a1 = np.array([
#     [1, 1, 2],
#     [1, 1, 2],
#     [1, 1, 2]
# ])
#
# a2 = np.array([
#     [1, 0, 0],
#     [2, 0, 0],
#     [1, 0, 0]
# ])
#print(np.dot(a1, a2))
