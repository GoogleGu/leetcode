# author: Arthur Gu
# date: 2018.12.8
from lib.testutil import runtime
from math import sqrt
from collections import defaultdict


def prime_factors(n):
    """
    比较pythonic的方法，使用defaultdict来计数，也可以用Counter。
    """
    results = defaultdict(lambda: 0)
    num = n
    # 从2到根号n，逐个寻找质因子
    for i in range(2, int(sqrt(n))+1):
        if num < i:  # 如果商已经小于当前的i时，已不可能再出现新的质数，直接退出
            break
        while num % i == 0:
            results[i] += 1
            num = num / i
    # 计算是否漏了最大的一个质因子
    product = 1
    for factor, count in results:
        product *= factor ** count
    if n / product > 1:
        results[int(n / product)] += 1
    output = ''.join('({}{})'.format(factor, '**{}' % count if count > 1 else '')
                     for factor, count in sorted(list(results.items()), key=lambda x: x[0]))
    return output


def prime_factors_vanila(n):
    """
    不使用python特性的方法，使用数组列表来计数。
    """
    results = [[1, 1]]
    num = n
    # 从2到根号n，逐个寻找质因子
    for i in range(2, int(sqrt(n))+1):
        if num < i:  # 如果商已经小于当前的i时，已不可能再出现新的质数，直接退出
            break
        while num % i == 0:
            if results[-1][0] != i:
                results.append([i, 1])
            else:
                results[-1][1] += 1
            num = num / i
    # 计算是否漏了最大的一个质因子
    product = 1
    for factor, count in results[1:]:
        product *= factor ** count
    if n / product > 1:
        results.append([int(n / product), 1])
    # 输出结果
    output = ''.join('({}{})'.format(factor, '**{}' % count if count > 1 else '')
                     for factor, count in results[1:])
    return output


def highest_vote(n):
    ret = ''
    for i in range(2, n + 1):
        num = 0
        while n % i == 0:
            num += 1
            n /= i
        if num > 0:
            ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return ret


if __name__ == '__main__':
    num = 12379341134
    num = 2147483647
    runtime(prime_factors_vanila, num, run_count=100)
    # runtime(highest_vote, num, run_count=10)
