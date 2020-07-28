# chi-square test 卡方检验

"""
$\\Chi^2$ 这个是希腊字母Chi，看起来像大写的X。
卡方分布是一种连续概率分布。
如果有一个变量Z服从标准正态分布，那么Z^2符合自由度为1的卡方分布
""" 

# from scipy.stats import chisquare
# import numpy as np


observed = [5, 82, 251] 
expected = [13.52, 108.16, 216.32]

def get_chisquare_statistic(observed, expected):
    """
    计算卡方分布的统计量
    """
    n = len(observed)
    X2 = 0
    for i in range(n):
        X2 += (observed[i] - expected[i])**2 / expected[i]
    return X2


X2 = get_chisquare_statistic(observed, expected)
print(X2)
