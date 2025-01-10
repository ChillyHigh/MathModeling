# 求解线性规划问题

import numpy as np
from scipy import optimize


# 定义目标函数的系数


result = optimize.linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)