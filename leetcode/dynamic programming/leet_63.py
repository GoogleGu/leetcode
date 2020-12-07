"""
不同路径 II

链接：https://leetcode-cn.com/problems/unique-paths-ii

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
"""
import pprint

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        max_col = len(obstacleGrid[0])
        max_row = len(obstacleGrid)
        paths = [[0 for i in range(max_col)] for j in range(max_row)]
        paths[-1][-1] = 0 if obstacleGrid[-1][-1] else 1
        # 初始化下底边和右边
        for i in range(max_col-2, -1, -1):
            if not obstacleGrid[-1][i]:
                paths[-1][i] = paths[-1][i+1]
        for i in range(max_row-2, -1, -1):
            if not obstacleGrid[i][-1]:
                paths[i][-1] = paths[i+1][-1]

        for row in range(max_row-2, -1, -1):
            for col in range(max_col-2, -1, -1):
                if not obstacleGrid[row][col]:
                    paths[row][col] += paths[row][col+1]
                    paths[row][col] += paths[row+1][col]
        return paths[0][0]


if __name__ == '__main__':
    input = [
        [0,0],
        [1,1],
        [0,0]
    ]
    print(Solution().uniquePathsWithObstacles(input))