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
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            results.add(i)
            results.add(int(n/i))
    return sum(num*num for num in results)

# ------------------- 最高票答案 -------------------- #
CACHE = {}


def squared_cache(number):
    if number not in CACHE:
        divisors = [x for x in range(1, number + 1) if number % x == 0]
        CACHE[number] = sum([x * x for x in divisors])
        return CACHE[number]

    return CACHE[number]


def highest_vote(m, n):
    ret = []

    for number in range(m, n + 1):
        divisors_sum = squared_cache(number)
        if (divisors_sum ** 0.5).is_integer():
            ret.append([number, divisors_sum])

    return ret

# ---------------------------------------------------- #

if __name__ == '__main__':
    print(list_squared(1, 250))
