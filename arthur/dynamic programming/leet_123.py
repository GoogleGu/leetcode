class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        profits = [[-1000000 for i in range(5) ] for _ in range(len(prices))]
        profits[0][0] = 0
        profits[0][1] = -prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            profits[i][0] = profits[i-1][0]  # 从来没买
            profits[i][1] = max(profits[i-1][0]-price, profits[i-1][1])  # 买了一笔
            profits[i][2] = max(profits[i-1][1]+price, profits[i-1][2])  # 卖了一笔
            profits[i][3] = max(profits[i-1][2]-price, profits[i-1][3])  # 买了两笔
            profits[i][4] = max(profits[i-1][3]+price, profits[i-1][4])  # 卖了两笔
        return max(profits[-1])

