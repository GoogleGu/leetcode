class Solution:
    def largest1BorderedSquare(self, grid):
        max_len = 0  # 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 每次从已知最大边长的正方形开始尝试
                temp_len = max_len
                # 如果上左边全是1，则尝试判断下右边
                while grid[i][j] and self.upper_edges_are_okay(grid, j, i, temp_len):
                    # 如果下右边全是1，则当前边长可以，将当前边长更新为最大长度
                    # 即便下右边不全是1，也可能有更大边长的正方形存在，所以继续增加尝试的长度而不直接break
                    if self.lower_edges_are_okay(grid, j, i, temp_len):
                        max_len = temp_len
                    temp_len += 1

        return max_len * max_len

    def upper_edges_are_okay(self, grid, x, y, edge_len):
        """ 判断长度为edge_len的上左边是否全是1 """
        try:
            for i in range(x+1, x + edge_len):
                if not grid[y][i]:
                    return False
            for j in range(y+1, y + edge_len):
                if not grid[j][x]:
                    return False
        except IndexError:
            return False
        return True

    def lower_edges_are_okay(self, grid, x, y, edge_len):
        """ 判断长度为edge_len的下右边是否全是1 """
        try:
            for i in range(x + edge_len - 1, x - 1, -1):
                if not grid[y+edge_len - 1][i]:
                    return False
            for j in range(y + edge_len - 1, y - 1, -1):
                if not grid[j][x+edge_len - 1]:
                    return False
        except IndexError:
            return False
        return True
