""" https://leetcode-cn.com/problems/range-sum-query-2d-immutable/ """


class NumMatrix:

    def __init__(self, matrix):
        self.cumulated = matrix
        if not len(self.cumulated) or not len(self.cumulated[0]):
            return 
        m, n = len(self.cumulated), len(self.cumulated[0])
        for i in range(1, m):
            self.cumulated[i][0] += self.cumulated[i-1][0]
        for j in range(1, n):
            self.cumulated[0][j] += self.cumulated[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                top_left = self.cumulated[i-1][j-1]
                left = self.cumulated[i-1][j]
                top = self.cumulated[i][j-1]
                self.cumulated[i][j] = self.cumulated[i][j] + left + top - top_left

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total_sum = self.cumulated[row2][col2]
        if row1 > 0 and col1 > 0:
            total_sum += self.cumulated[row1-1][col1-1]
        if col1 > 0:
            total_sum -= self.cumulated[row2][col1-1]
        if row1 > 0:
            total_sum -= self.cumulated[row1-1][col2]
        return total_sum
