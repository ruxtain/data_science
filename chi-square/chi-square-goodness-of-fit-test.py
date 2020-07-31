# chi-square test 卡方检验

"""
$\\Chi^2$ 这个是希腊字母Chi，看起来像大写的X。
卡方分布是一种连续概率分布。
如果有一个变量Z服从标准正态分布，那么Z^2符合自由度为1的卡方分布
""" 

from scipy.stats import chisquare

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

# 本来打算传入X2后计算p-value的，但是这个函数很直接，传入原始
output = chisquare(observed, expected)
print(output.statistic, output.pvalue)


# 如果根据数据推断均值，则损失一个额外的自由度，因此 ddof = 1
# 自由度 = number of cells - 1 - ddof
observed = [5, 82, 251] 
expected = [6.26, 79.48, 252.26]
output = chisquare(observed, expected, ddof=1)
print(output.statistic, output.pvalue)
