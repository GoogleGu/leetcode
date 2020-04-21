class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        num_matrix = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]

        max_len = max(num_matrix[0])
        for i in range(1, len(num_matrix)):
            max_len = max(max_len, num_matrix[i][0])
        for row in range(1, len(num_matrix)):
            for col in range(1, len(num_matrix[0])):
                if num_matrix[row][col] != 0:
                    num_matrix[row][col] = min(num_matrix[row-1][col-1], num_matrix[row-1][col], num_matrix[row][col-1]) + 1
                    max_len = max(max_len, num_matrix[row][col])

        return max_len * max_len


if __name__ == '__main__':
    input = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(Solution().maximalSquare(input))