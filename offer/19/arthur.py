# -*- coding:utf-8 -*-
from math import ceil

class Solution:
    # matrix类型为二维列表，需要返回列表

    def printMatrix(self, matrix):
        # 处理特殊情况
        if not matrix:
            return
        y = len(matrix)
        if y == 0:
            return
        x = len(matrix[0])

        edge_limit = x if x < y else y
        max_offset = ceil(edge_limit / 2)

        # 进行矩阵输出
        helix = []
        for offset in range(max_offset):
            # 输出上边
            helix.extend(matrix[offset][offset:(x-offset)])
            # 输出右边
            for rows in matrix[(offset+1):(y-offset-1)]:
                helix.append(rows[x-offset-1])
            # 输出下边
            if y - offset - 1 != offset:
                helix.extend(matrix[y-offset-1][offset:(x-offset)][::-1])
            # 输出左边
            for rows in matrix[(offset+1):(y-offset-1)][::-1]:
                helix.append(rows[offset])
        return helix


if __name__ == '__main__':
    input_mat = [
        [1,2,3,4],
        [4,5,6,8],
        [7,8,9,0],
        [11,12,13,14],
        [21,22,23,24],
    ]

    print(Solution().printMatrix(input_mat))


