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

# @pysnooper.snoop()
def partition(tinput, start, end):
        first_big_num_index = start
        for i in range(start, end):
            if tinput[i] < tinput[end]:
                tinput[i], tinput[first_big_num_index] = tinput[first_big_num_index], tinput[i]
                first_big_num_index += 1
        tinput[end], tinput[first_big_num_index] = tinput[first_big_num_index], tinput[end]
        return first_big_num_index


if __name__ == '__main__':
    solution = Solution()
    input = [9,4,7,8,3,6,43]
    solution.GetLeastNumbers_Solution(input, k=4)