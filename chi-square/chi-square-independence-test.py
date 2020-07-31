"""
参考我的简书笔记：卡方检验详解
数据如下表，括号是原假设下的值：
|                      | Never  | Occasional | Frequent | Row total |
|----------------------|--------|------------|----------|-----------|
|Trouble with police   |71      |154         |398       |623        |
|                      |(282.6) |(165.4)     |(175.0)   |           |
|No trouble with police|4992    |2808        |2737      |10537      |
|                      |(4780.4)|(2796.6)    |(2960.0)  |           |
|Column total          |5063    |2962        |3135      |11160      |
"""

#于是我们可以计算统计量：

observed = [71, 154, 398, 4992, 2808, 2737]
expected = [282.6, 165.4, 175.0, 4780.4, 2796.6, 2960.0]

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

# 和 goodness of fit 的过程其实是一样的

from scipy.stats import chisquare

observed = [71, 154, 398, 4992, 2808, 2737]
expected = [282.6, 165.4, 175.0, 4780.4, 2796.6, 2960.0]

output = chisquare(observed, expected)
print('statistic: {:.2f}, pvalue: {:.4f}'.format(output.statistic, output.pvalue))
