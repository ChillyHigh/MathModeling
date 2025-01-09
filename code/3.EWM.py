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
            a = int(input("请输入区间型数据的下限:"))
            b = int(input("请输入区间型数据的上限:"))
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

# 计算信息熵
Z = data.iloc[:,1:]
P = Z / Z.sum(axis=0) # axis=0表示按列求和
# 由于ln(0)不存在，所以将0替换为1e-10
P[P == 0] = 1e-10
H = -np.sum(P*np.log(P),axis=0)
e_j = H/np.log(n)
d_j = 1 - e_j
w = d_j / d_j.sum(axis=0)
print("权值为：")
print(w)

