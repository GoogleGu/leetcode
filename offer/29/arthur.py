
class Solution:
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


def partition(tinput, start, end):
        j = start - 1
        cmp = tinput[end]
        for i in range(start, end):
            if tinput[i] < cmp:
                j += 1
                tinput[i], tinput[j] = tinput[j], tinput[i]
        j += 1
        tinput[end], tinput[j] = tinput[j], tinput[end]
        return j
