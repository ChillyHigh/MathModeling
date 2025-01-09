import numpy as np
import pandas as pd
import math


# 算数平均法求权重
a = input("请输入判断矩阵：")
a = np.array(eval(a))
sum_a = np.sum(a, axis=0)
stand_a = a / sum_a
w1 = np.sum(stand_a, axis=1) / np.size(stand_a, axis=1)

print(w1)

# 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(a)

# 特征向量归一化
weights = eigenvectors[:, np.argmax(eigenvalues)]
weights /= np.sum(weights)

print("计算得到的权重：", weights)

# 计算一致性比率CI
CI = (max(eigenvalues) - len(a)) / (len(a) - 1)
print("CI：", CI)
RI = [0, 0.0001, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]
CR = CI / RI[len(a) - 1]
print("CR：", CR)
if CR < 0.1:
    print("判断矩阵通过一致性检验")
else:
    print("判断矩阵未通过一致性检验")