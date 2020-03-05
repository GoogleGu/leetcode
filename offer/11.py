import math


class Solution:

    max_num = int(math.pow(2, 32))

    def number_of_one(self, n):
        count = 0
        quotient = n if n > 0 else self.suplement(n)
        while quotient > 0:
            remainder = quotient % 2
            if remainder == 1:
                count += 1
            quotient = quotient // 2
        return count

    def suplement(self, n):
        """ 补码对应的数 = 2^最大位数 - 原数的模 """
        return self.max_num + n

if __name__ == '__main__':
    solution = Solution()
    print(solution.number_of_one(-1))
