class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        """
        用递归的思想，优先用礼包来买，并在买各个礼包的选择上用动态规划，最终终结状态是无礼包可用，用正常单价完成购物
        只不过这个题的动态转移方程比较难表达出来。
        """

        def shopping(special, needs):  
            # 从special里刚好购买needs所需的最低花费
            if sum(needs) == 0:  
                return 0
            # 先过滤掉special里已经有某一种物品超过了needs的礼包
            valid_special = []
            for package in special:
                if all(package[i] <= needs[i] for i in range(n)):
                    valid_special.append(package)

            # 如果过滤后为空，那么返回直接以单品购买needs的价格
            if not valid_special: 
                return sum(needs[i] * price[i] for i in range(n))

            # 动态规划，收集本次购买每种礼包的花费加上若购买该礼包后剩余needs递归的最低花费
            res = []
            for package in valid_special:  
                res.append(package[-1] + shopping(valid_special, [needs[i] - package[i] for i in range(n)]))
            return min(res)  

        n = len(price)
        # 先过滤掉不比原价买划算的礼包
        valid_special = []
        for package in special:
            normal_price = sum(package[i] * price[i] for i in range(n))
            if package[-1] <= normal_price:
                valid_special.append(package)
        
        # 开始买
        return shopping(valid_special, needs)