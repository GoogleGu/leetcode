class Solution:
    def FindNumbersWithSum(self, array, tsum):
        left = 0
        right = len(array) - 1

        while True:
            if left >= right:
                return []
            if array[left] + array[right] == tsum:
                return [array[left], array[right]]
            elif array[left] + array[right] > tsum:
                right -= 1
            elif array[left] + array[right] < tsum:
                left += 1
        # 2 + 8 / 4 + 6 / (2+x)(8-x) / 6x >= x*x
        # so 是第一个
