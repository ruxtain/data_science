"""
时间: 2020-07-26 23:46
完成度: 60%
概述: 简单介绍了bootstrap的大致步骤，但是还不够深入，需要进一步完善，总结到可以为A/B test直接服务的程度
"""


import scipy.stats
import numpy as np
import sklearn

# 已知数据
data = np.array([30, 37, 36, 43, 42, 48, 43, 46, 41, 42])

# 样本均值即为估计总体均值的最优解
mean = data.mean()


# 更进一步的问题，请计算置信水平为80%的置信区间

# Traditional Method
# 这里直接用t分布计算双侧置信区间
# 具体而言，就是用样本的均值和标准差估算总体的分布，我们认为总体是一个t分布
# 研究表明，总体即使显著偏离正态分布，用t分布计算置信区间仍然是比较准确的，这部分的原理先不深究

std = data.std()
degree_of_freedom = len(data) - 1

interval = scipy.stats.t.interval(0.8, degree_of_freedom, mean, std)
print('t-distribution:', interval)

# Bootstrap Method
# 通过重采样的方式获取模拟数据，然后根据模拟数据的参数的均值估算总体的参数
# 参考文章：https://zhuanlan.zhihu.com/p/41099219

sample_size = len(data) # 显然，重采样的样本量（bootstrap样本量）必须小于等于原始样本量
boot = sklearn.utils.resample(data, replace=True, n_samples=sample_size, random_state=42)

# 进行n次重采样，获得n个bootstrap样本
n = 200
boot_means = []
for i in range(200):
    boot = sklearn.utils.resample(data, replace=True, n_samples=sample_size)
    boot_means.append(boot.mean()-mean)

# 由于是80%的区间，所以取10分位和90分位的数据
boot_means.sort()
print('bootstrap:', mean-boot_means[180], mean-boot_means[19])

# Further reading
# 过程描述 https://machinelearningmastery.com/a-gentle-introduction-to-the-bootstrap-method/
# 命名缘由 https://www.thoughtco.com/what-is-bootstrapping-in-statistics-3126172



