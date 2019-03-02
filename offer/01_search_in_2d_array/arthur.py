# -*- coding:utf-8 -*-
class Solution:

    # array 二维列表
    def find(self, target, array):
        """
        列与排步进查找
        复杂度M+N（M与N为array的长与宽）
        运行时间：424ms
        占用内存：5704k
        """
        if array:
            rows = len(array)
            columns = len(array[0])
            row = 0
            column = columns - 1
            while row < rows and column >= 0:
                if array[row][column] == target:
                    return True
                elif array[row][column] > target:
                    column -= 1
                else:
                    row += 1
        return False

    def binary_find(self, target, array):
        """
        逐排/列二分查找
        为了节约时间，将较长的轴定为二分查找的轴。
        算法复杂度MlogN（M为较短的一边，N为较长的一边）
        运行时间: 216 ms
        占用内存: 5728K
        """

        if array:
            # 判断是逐排二分查找还是逐列二分查找
            rows = len(array)
            columns = len(array[0])
            if rows > columns:
                # 逐列二分查找
                for column in range(columns):
                    if array[0][column] <= target <= array[rows-1][column]:
                        if self._column_binary_search(target, array, column, rows):
                            return True
            else:
                #逐行二分查找
                for row in range(rows):
                    if array[row][0] <= target <= array[row][columns-1]:
                        if self._row_binary_search(target, array, row, columns):
                            return True
        return False

    @staticmethod
    def _row_binary_search(target, matrix, row, columns):
        left_index = 0
        right_index = columns - 1
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            if matrix[row][middle_index] == target:
                return True
            elif matrix[row][middle_index] < target:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1
        return False

    @staticmethod
    def _column_binary_search(target, matrix, column, rows):
        left_index = 0
        right_index = rows - 1
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            if matrix[middle_index][column] == target:
                return True
            elif matrix[middle_index][column] < target:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1
        return False


if __name__ == '__main__':

    input = [[1,2,8,9],
             [2,4,9,12],
             [4,7,10,13],
             [6,8,11,15]]
    output = Solution().binary_find(1, input)
    print(output)