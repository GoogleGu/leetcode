import math

class Solution:

    dp = {0: 0, 1:1}    # 最佳分解数缓存
    squares = [1]   # 平方数缓存
    max_n = 1  # 已经算过的最大n的缓存

    def numSquares(self, n: int) -> int:
        self.squares.extend([i**2 for i in range(int(math.sqrt(self.squares[-1]))+1, int(math.sqrt(n))+1)])

        # 从之前的dp缓存最大数字对应的分解数一直算到要算的数字n对应的分解数
        for i in range(self.max_n + 1, n + 1):
            min_count = 10000000
            # 要计算当前i的最佳分解数，将其每一种拆解法都遍历一遍取最好的
            for square in self.squares:
                if square > i:
                    break
                min_count = min(min_count, self.dp[i-square] + 1)
            self.dp[i] = min_count

        # 更新max_n
        self.max_n = max(n, self.max_n)

        return self.dp[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(7680))