"""
致谢：
感谢这位大佬的代码：https://github.com/mvanga/pybootstrap

为什么叫Bootstrap这么奇葩的名字？
https://www.thoughtco.com/what-is-bootstrapping-in-statistics-3126172
"""

import numpy as np
import scipy.stats
from sklearn.utils import resample
from random import sample


def bootstrap_ci(dataset, confidence=0.95, iterations=10000, sample_size=1.0, statistic=np.mean):
    """
    Bootstrap the confidence intervals for a given sample of a population
    and a statistic. "ci" as in "confidence interval".
    Args:
        dataset: A list of values, each a sample from an unknown population
        confidence: The confidence value (a float between 0 and 1.0)
        iterations: The number of iterations of resampling to perform
        sample_size: The sample size for each of the resampled (0 to 1.0
                     for 0 to 100% of the original data size)
        statistic: The statistic to use. This must be a function that accepts
                   a list of values and returns a single value.
    Returns:
        Returns the upper and lower values of the confidence interval.
    """
    stats = list()
    n_size = int(len(dataset) * sample_size)

    for _ in range(iterations):
        # 虽然replace默认为True，但是这里专门写出来表示强调bootstrap的抽样是有放回的抽样
        # replace=True时，显然你的bootstrap样本可以大于原样本，而replace=False，你的bootstrap样本最多和原样本一样大，因为你抽光了所有元素
        sample = resample(dataset, replace=True, n_samples=n_size)
        # statistic是你要计算的“统计量”(https://en.wikipedia.org/wiki/Statistic)
        # 统计量是统计理论中用来对数据进行分析、检验的变量
        # 比如均值是一种统计量
        stat = statistic(sample)
        # 将每一次bootstrap的抽样放入统计量列表stats
        stats.append(stat)

    # 将统计量进行排序，根据置信水平，选择合适的分位数，作为置信区间的两端
    # 看起来这样的操作的本质是通过bootstrap制造一个虚拟的总体，然后直接根据置信水平确定置信区间
    ostats = sorted(stats)
    lval = np.percentile(ostats, ((1 - confidence) / 2) * 100)
    uval = np.percentile(ostats, (confidence + ((1 - confidence) / 2)) * 100)

    return (lval, uval)


def ttetst_ci(dataset, confidence=0.95):
    """
    为了和bootstrap的区间估计进行对比，这里直接用t分布计算双侧置信区间
    研究表明，总体即使显著偏离正态分布，用t分布计算置信区间仍然是比较准确的，这部分的原理先不深究
    """
    # 样本均值即为估计总体均值的最优解
    mean = dataset.mean()
    
    # 更进一步的问题，请计算置信水平为confidence的置信区间
    std = dataset.std()

    # 自由度为样本量-1
    degree_of_freedom = len(dataset) - 1

    interval = scipy.stats.t.interval(confidence, degree_of_freedom, mean, std)
    return interval


def comparison(pop_dist='normal', sample_size=100):
    """
    进一步的，我们对一个已知总体（指数分布、正态分布两种）进行抽样，然后来看两种区间估计方式哪一种更加准确
    pop_dist: normal distribution 正态分布
              exponential distribution 指数分布

    如果想要查看两种分布的图象，可以参考下面的代码：
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    exp_pop = np.random.exponential(1, 10000) # normal与之类似
    df = pd.DataFrame(exp_pop)
    df.hist()
    """
    if pop_dist == 'normal':
        pop = np.random.normal(167.1, 5.7, 10000) # 参数分别是: 均值、标准差、元素个数，此为2012年中国男性身高分布

    elif pop_dist == 'exponential':
        pop = np.random.exponential(1, 10000) # 第一个参数beta=1时，该分布是 e^(-x) 函数的分布

    sam = sample(list(pop), sample_size) # 抽样100个
    sam = np.array(sam)

    print('\t总体均值:', pop.mean())
    print('\tbootstrap 置信区间', bootstrap_ci(sam, confidence=0.9, iterations=10000))
    print('\tttest 置信区间', ttetst_ci(sam, confidence=0.9))





if __name__ == '__main__':

    # data = np.array([30, 37, 36, 43, 42, 48, 43, 46, 41, 42])
    # print(bootstrap_ci(data, confidence=0.8, iterations=10000))
    # print(ttetst_ci(data, confidence=0.8))

    print('正态分布的估计')
    comparison(pop_dist='normal', sample_size=10)
    print()
    print('指数分布的估计')
    comparison(pop_dist='exponential', sample_size=10)

"""
一点笔记：
iterations 要多少合适呢？
经过测试，对于本例，iterations在10000次时，置信区间趋于稳定，因此也不是越多越好，合适就行

哪种方式更优？
经过计算发现，bootstrap给出的置信区间更加狭窄，且较为准确，没有出现总体均值落在置信区间以外的状况。

一点感悟：
对于一个完全不知道总体是什么分布的数据，随便抓一把数据出来，就能利用bootstrap比较准确地估算其总体均值的范围，真的很神奇。
即使样本量很小，bootstrap表现依旧不俗。
"""
