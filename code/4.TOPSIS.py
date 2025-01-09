import numpy as np
import pandas as pd

data = pd.read_excel('code\data.xlsx')

### 1.数据正向化
vec = input("请输入需要正向化的向量组，以数组形式输入，如[1,2,3]表示1,2,3列需要正向化，不需要正向化输入-1:\n")
if vec != '-1':
    vec = eval(vec)
    print(data.dtypes)
    for i in vec:
        flag = input("第{}列({})是哪一类数据？(1.极小型 2.中间型 3.区间型):".format(i,data.columns[i]))
        if flag == '1': # 极小型
            data.iloc[:,i] = data.iloc[:,i].max() - data.iloc[:,i]
        elif flag == '2':
            mid = float(input("请输入中间型数据的最好值:"))
            M = abs(data.iloc[:,i] - mid).max()
            data.iloc[:,i] = 1 - abs(data.iloc[:,i] - mid)/M
        elif flag == '3':
            a = float(input("请输入区间型数据的下限:"))
            b = float(input("请输入区间型数据的上限:"))
            M = max(a - data.iloc[:,i].min(), data.iloc[:,i].max() - b)# $M={\rm max}\{a-{\rm min}\{x_i\},{\rm max}\{x_i\}-b\}$
            for j in range(len(data.iloc[:,i])): #$\tilde{x}=\begin{cases}1-\frac{a-x_i}{M}, & x_i<a\\1,&a\leq x_i \leq b\\1-\frac{x_i-b}{M}, &x_i>b\end{cases}$
                if data.iloc[j,i] < a:
                    data.iloc[j,i] = 1 - (a - data.iloc[j,i]) / M
                elif data.iloc[j,i] <= b:
                    data.iloc[j,i] = 1
                else:
                    data.iloc[j,i] = 1 - (data.iloc[j,i] - b) / M
print(data)

# 标准化处理
[n,m] = data.shape
# 检查负数
isNeg = 0
for i in range(1,m):
    if data.iloc[:,i].min() < 0:
        isNeg = 1
        break
if isNeg == 1:
    for i in range(1,m):
        data.iloc[:,i] = (data.iloc[:,i] - data.iloc[:,i].min())/(data.iloc[:,i].max() - data.iloc[:,i].min())
else:
    for i in range(1,m):
        squareSum = np.sum(data.iloc[:,i]**2)
        data.iloc[:,i] = data.iloc[:,i]/np.sqrt(squareSum)
print(data)

# 用优劣打分
Z = data.iloc[:,1:]
Z_plus = Z.copy()
Z_minus = Z.copy()
for i in range(m-1):
    Z_plus.iloc[:,i] = np.max(Z.iloc[:,i])
    Z_minus.iloc[:,i] = np.min(Z.iloc[:,i])
print(Z_plus)
print(Z_minus)

D_plus = np.sqrt(np.sum((Z - Z_plus)**2,axis=1))
D_minus = np.sqrt(np.sum((Z - Z_minus)**2,axis=1))
S = D_minus / (D_plus + D_minus)
print(S)