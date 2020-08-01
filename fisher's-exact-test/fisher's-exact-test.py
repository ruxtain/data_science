"""
参考: https://www.jianshu.com/p/fcfac399de13
"""

def factorial(n:int):
    """阶乘函数"""
    s = 1
    while n > 1:
        s *= n
        n -= 1
    return s

def C(m:int, n:int):
    """组合数公式。C(m, n)表示$C_m^n$"""
    return factorial(m) / (factorial(m-n)*factorial(n))

# print('p-value = {:.4f}%'.format(C(10,10)/C(20,10)*100))

# print('p-value = {:.4f}%'.format((C(4,1)*C(4,3))/C(8,4)*100))


from scipy.stats import fisher_exact

# 列联表
contigency_table = [[0, 4], [4, 0]]

# alternative 表示备择假设
# alternative='less' 表示零假设是相等，备择假设是
oddsratio, pvalue = fisher_exact(contigency_table, alternative='less')
print(pvalue)






