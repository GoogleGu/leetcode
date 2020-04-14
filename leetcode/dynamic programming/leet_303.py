class NumArray:

    def __init__(self, nums):
        self.sums = [0 for _ in range(len(nums)+1)]

        for i in range(1, len(nums)+1):
            self.sums[i] = self.sums[i-1] + nums[i-1]

    def sumRange(self, i: int, j: int):
        return self.sums[j+1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
obj = NumArray([-2,0,3,-5,2,-1])
param_1 = obj.sumRange(0, 3)
print(obj.sums)
print(param_1)