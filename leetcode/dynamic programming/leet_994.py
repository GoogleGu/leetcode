"""
9腐烂的橘子
https://leetcode-cn.com/problems/rotting-oranges

在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。


提示：

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] 仅为 0、1 或 2

"""

class Solution:
    def orangesRotting(self, grid):
        t = 0
        col_len = len(grid)
        row_len = len(grid[0])
        rottens = [(i, j) for i in range(col_len) for j in range(row_len) if grid[i][j] == 2]

        # 在一开始就没有烂橘子的情况下，最后t会多减一次1，因此加上
        if not rottens:
            t += 1

        # 模拟每轮烂橘子传染的过程，直到没有新的橘子被传染为止
        while rottens:
            # print(t)
            # print(rottens)
            t += 1
            new_rottens = []
            for i, j in rottens:
                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    new_rottens.append((i-1, j))
                if i+1 < col_len and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    new_rottens.append((i+1, j))
                if j-1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    new_rottens.append((i, j-1))
                if j+1 < row_len and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    new_rottens.append((i, j+1))
            rottens = new_rottens

        # 最后阶段，如果还有好橘子存在，则说明有好橘子无法被传播
        for row in grid:
            if 1 in row:
                return -1

        # 否则，返回t-1，因为在模拟阶段实际上多跑了一轮
        return t-1


if __name__ == '__main__':
    Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
