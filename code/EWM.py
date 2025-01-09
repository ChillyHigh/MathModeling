import numpy as np
import pandas as pd

data = pd.read_excel('code\data.xlsx')

vec = input("请输入需要正向化的向量组，以数组形式输入，如[1,2,3]表示1,2,3列需要正向化，不需要正向化输入-1\n")
if vec != '-1':
    vec = eval(vec)
    for i in vec:
        flag = input("第{}列({})是哪一类数据(1.极小型 2.中间型 3.区间型)".format(i,data.columns[i]))
        if flag == '1':
            data.iloc[:,i] = data.iloc[:,i].max() - data.iloc[:,i]
            print(data)