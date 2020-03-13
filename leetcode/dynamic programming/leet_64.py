"""
最小路径和

链接：https://leetcode-cn.com/problems/minimum-path-sum

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""

class Solution:
    def minPathSum(self, grid):
        for row in range(1, len(grid[0])):
            grid[0][row] += grid[0][row-1]
        for col in range(1, len(grid)):
            grid[col][0] += grid[col-1][0]

        for col in range(1, len(grid)):
            for row in range(1, len(grid[0])):
                grid[col][row] += min(grid[col-1][row], grid[col][row-1])

        return grid[-1][-1]
