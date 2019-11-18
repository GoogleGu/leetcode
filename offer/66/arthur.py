# -*- coding:utf-8 -*-
class Solution:
    count = 0
    def movingCount(self, threshold, rows, cols):
        
        self.count = 0
        # 创建二维数组代表地图
        field = [[0 for col in range(cols)] for row in range(rows)]
        self.check_cell(0, 0, field, threshold)
        return self.count
    
    def check_cell(self, col, row, field, threshold):
        if col < 0 or row < 0 or col >= len(field[0]) or row >= len(field):
            return 
        if field[row][col] != 0:
            return

        col_sum = sum(int(digit) for digit in list(str(col)))
        row_sum = sum(int(digit) for digit in list(str(row)))
        if col_sum + row_sum <= threshold:
            self.count += 1
            field[row][col] = 1
            self.check_cell(col+1, row, field, threshold)
            self.check_cell(col-1, row, field, threshold)
            self.check_cell(col, row+1, field, threshold)
            self.check_cell(col, row-1, field, threshold)
            


if __name__ == "__main__":
    result = Solution().movingCount(1, 2, 2)
    print(result)