# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if not data:
            return 0
        return self.middle(data, k)

    def middle(self, data, k):
        middle = len(data) // 2
        if middle == 0:
            if data[middle] == k:
                return 1
            return 0
        if data[middle] > k:
            return self.middle(data[:middle], k)
        elif data[middle] < k:
            return self.middle(data[middle:], k)
        else:
            left_count = self.get_left_count(data[:middle], k)
            right_count = self.get_right_count(data[middle:], k)
            return left_count + right_count

    def get_left_count(self, data, k):
        count = 0
        for index in range(-1, -len(data)-1, -1):
            if data[index] == k:
                count += 1
            else:
                return count
        return count

    def get_right_count(self, data, k):
        count = 0
        for index in data:
            if index == k:
                count += 1
            else:
                return count
        return count


print(Solution().GetNumberOfK([1,3,3,3,3,4,5], 2))
