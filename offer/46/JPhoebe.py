# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n <= 0:
            return -1

        # 每一标准下标定义为x
        # 0  ~  n-1

        # 每一项散乱后定义为x'
        # 去除一个数k【(m-1)%n】后
        # k+1  ~  n-1  0  ~  k-1

        # 将下标转换为0 ~ (n-1)的问题
        # f(n, m)

        # f'(n-1, m)
        # 左移k+1(会有负数)
        # p(x') = (x'-k-1)%n
        # 右移k+1
        # p-1(x') = (x'+k+1)%n

        # 剩下的数的下标相等
        # f(n, m) = f'(n-1, m)

        res = 0
        for i in range(1, n + 1, 1):
            res = (res + m) % i
        return res


print(Solution().LastRemaining_Solution(5, 3))




