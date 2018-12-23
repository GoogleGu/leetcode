# author: Arthur
# date: 2018.12.23

import math


def list_squared(m, n):
    """ main function. """
    specials = []
    for i in range(m, n+1):
        sums = sum_of_factors(i)
        if '{}'.format(math.sqrt(sums))[-1] == '0':
            specials.append([i, sums])
    return specials


def sum_of_factors(n):
    """ Helper function that compute sum of factors of number n. """
    results = set()
    if n == 1:
        return 1
    # 从1到n/2，逐个寻找因子
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            results.add(i)
            results.add(int(n/i))
    return sum(num*num for num in results)


if __name__ == '__main__':
    print(list_squared(42, 250))