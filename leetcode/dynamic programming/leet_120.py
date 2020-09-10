class Solution:
    """
    直接使用维特比算法
    """

    def minimumTotal(self, triangle):
        for row in range(1, len(triangle)):
            triangle[row][0] += triangle[row-1][0] 
            for col in range(1, len(triangle[row])-1):
                triangle[row][col] += min(triangle[row-1][col], triangle[row-1][col-1])
            triangle[row][-1] += triangle[row-1][-1]
        
        return min(triangle[-1])



if __name__ == "__main__":
    tri = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
    print(Solution().minimumTotal(tri))