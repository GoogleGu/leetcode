class Solution:
    def recursive_largestRectangleArea(self, heights):
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]

        min_height = min(heights)
        min_index = heights.index(min_height)

        area1 = min_height * len(heights)
        left_max = self.recursive_largestRectangleArea(heights[:min_index])
        right_max = self.recursive_largestRectangleArea(heights[min_index+1:])
        return max(area1, left_max, right_max)

    def largestRectangleArea(self, heights):
        """
        用单调栈结构来解决问题
        """
        stack = [-1]
        max_area = 0
        heights.append(-1)
        for i in range(len(heights)):
            while len(stack) > 1 and heights[stack[-1]] >= heights[i]:
                max_area = max(heights[stack.pop()] * (i - stack[-1] -1), max_area)
            stack.append(i)
        return max_area


if __name__ == '__main__':
    print(Solution().largestRectangleArea([2,1,2]))
