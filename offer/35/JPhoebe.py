# -*- coding:utf-8 -*-
class Solution:
    result = 0

    def InversePairs(self, data):
        self.MergeSort(data)
        return self.result % 1000000007

    def MergeSort(self, lists):
        if len(lists) <= 1:
            return lists
        num = int(len(lists) / 2)
        left = self.MergeSort(lists[:num])
        right = self.MergeSort(lists[num:])
        return self.Merge(left, right)

    def Merge(self, left, right):


        r, l = 0, 0
        temp = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                temp.append(left[l])
                l += 1
            else:
                temp.append(right[r])
                r += 1
                self.result += len(left) - l
        temp += list(left[l:])
        temp += list(right[r:])
        return temp

print(Solution().InversePairs([3, 1, 5, 1, 1, 1]))
# print(Solution().InversePairs(
#     [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601, 650, 418, 355, 460, 505, 360,
#      965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550, 474, 162, 268, 142,
#      463, 221, 882, 576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983, 583, 523, 697, 478, 147, 795, 380,
#      973, 958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630, 425, 930, 64, 266, 235, 187, 284, 665,
#      874, 80, 45, 848, 38, 811, 267, 575]))
# print(Solution().InversePairs([5, 1, 7, 2, 3, 4]))
