"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵：
01 02 03 04
05 06 07 08
09 10 11 12
13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
[01,02,03,04,05],
[06,07,08,09,10],
[11,12,13,14,15],
[16,17,18,19,20],
[21,22,23,24,25]
"""

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        body = []
        x_size = len(matrix)
        y_size = len(matrix[0])
        init_x_length = x_size - 1
        init_y_length = y_size - 1
        x_length = init_x_length
        y_length = init_y_length
        total = x_size*y_size
        x = y = 0
        for i in range(0, total, 1):
            body.append(matrix[x][y])
            if y >= y_length:
                if x >= x_length:
                    y -= 1
                else:
                    x += 1
            else:
               temp = init_x_length - x_length
               if x == temp:
                   y += 1
               elif x <= x_length:
                   if y <= temp:
                       x -= 1
                       if x == y:
                           # 一圈结束
                           x += 1
                           y += 1
                           x_length -= 1
                           y_length -= 1
                   else:
                       y -= 1

        return body

matrix = [[1],[6],[11],[16],[21]]
print(Solution().printMatrix(matrix))


