class Solution:
    def maxProfit(self, prices):
        profit = 0
        bottom = 10000
        for num in prices:
            if num - bottom > profit:
                profit = num - bottom
            if num < bottom:
                bottom = num
        return profit
