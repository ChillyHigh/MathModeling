import numpy as np
import pandas as pd
import math

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])#定义矩阵
b = np.array([[1,0,0],[0,1,0],[0,0,1]])
print(a)
print(np.linalg.inv(a))#逆矩阵

# 特征值和特征向量
[V, D] = np.linalg.eig(a)
print(V)
print(D)
print(np.dot(a,b)) #矩阵乘法
print(a.sum())

#矩阵转置
print(a.T)