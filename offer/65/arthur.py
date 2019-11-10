# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        mat = [list(matrix[row_num*cols:row_num*cols+cols]) for row_num in range(rows)]
        for row in range(rows):
            for col in range(cols):
                val = mat[row][col]
                if val == path[0]:
                    mat[row][col] = '#'
                    if find_path(mat, path[1:], (row, col)):
                        return True
                    mat[row][col] = val
        return False


def find_path(mat, path, pos):
    if not path:
        return True

    possible_positoins = ((pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1))
    for row, col in possible_positoins:
        try:
            val = mat[row][col]
            if val == path[0]:
                mat[row][col] = '#'
                if find_path(mat, path[1:], (row, col)):
                    return True
                mat[row][col] = val
        except IndexError:
            continue
    return False



if __name__ == "__main__":
    results = Solution().hasPath("ABCESFCSADEE",3,4,"ABCCED")
    print(results)