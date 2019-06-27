import pysnooper


class Solution:


    @pysnooper.snoop()
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput) or k == 0:
            return []
        start = 0
        end = len(tinput) - 1
        index = -1
        while index != k-1:
            if index > k - 1:
                end = index - 1
            else:
                start = index + 1
            index = partition(tinput, start, end)
        return tinput[:k]

@pysnooper.snoop()
def partition(tinput, start, end):
        j = start
        cmp = tinput[end]
        for i in range(start, end):
            if tinput[i] < cmp:
                tinput[i], tinput[j] = tinput[j], tinput[i]
                j += 1
        tinput[end], tinput[j] = tinput[j], tinput[end]
        return j


if __name__ == '__main__':
    solution = Solution()
    input = [9,4,7,8,3,6,43]
    solution.GetLeastNumbers_Solution(input, k=4)