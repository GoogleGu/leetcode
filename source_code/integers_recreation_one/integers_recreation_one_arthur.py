# author: Arthur
# date: 2018.12.23

import math


def list_squared(m, n):
    """ main function. """
    specials = []
    for i in range(m, n+1):
        sums = sum_of_factors(i)
        if math.sqrt(sums).is_integer():
            specials.append([i, sums])
    return specials


def sum_of_factors(n):
    """ Helper function that compute sum of factors of number n. """
    results = {1, n}
    # 从1到n ** 0.5，逐个寻找因子
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            results.add(i)
            results.add(int(n/i))
    return sum(num*num for num in results)


if __name__ == '__main__':
    print(list_squared(1, 250))
