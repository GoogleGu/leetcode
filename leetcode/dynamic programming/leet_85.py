class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        max_area = 0
        heights = [0 for _ in range(len(matrix[0]))]
        heights.append(-1)
        for h in range(len(matrix)):
            for i in range(len(matrix[0])):
                if matrix[h][i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            print(heights)
            max_area = max(self.largestRectangleArea(heights), max_area)
        return max_area

    def largestRectangleArea(self, heights):
        """
        用单调栈结构来解决问题
        """
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while len(stack) > 1 and heights[stack[-1]] >= heights[i]:
                max_area = max(heights[stack.pop()] * (i - stack[-1] -1), max_area)
            stack.append(i)
        return max_area


if __name__ == '__main__':
    input = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(Solution().maximalRectangle(input))