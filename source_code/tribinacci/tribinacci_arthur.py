# author: Arthur Gu
# date: 2018.12.5

from functools import lru_cache


tribonacci_list = []

@lru_cache()
def tribonacci(seed, n):
    """
    使用lru_cache来缓存已经计算的结果，然后进行递归计算。
    由于还要保存之前计算过的结果，这种方式是比较蠢的，缓存和内存中各有一份已经计算的结果。建议使用下面的方法。
    """
    if n < 3:
        tribonacci_list.append(seed[n])
        return seed[n]
    else:
        this_num = tribonacci(seed, n-3) + tribonacci(seed, n-2) + tribonacci(seed, n-1)
        tribonacci_list.append(this_num)
        return this_num


def simple_tribonacci(seed, n):
    """
    拷贝一份初始化列表，每次计算出的新结果保存在初始化列表里，实现方式简单易读，推荐用这个。
    """
    result = list(seed.copy())
    if n > 3:
        for i in range(3, n):
            result.append(result[i-3] + result[i-2] + result[i-1])
    return result[:n]


if __name__ == '__main__':
    seed = [1, 1, 1]
    print(simple_tribonacci(seed, 10))

