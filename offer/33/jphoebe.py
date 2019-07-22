# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == 0: return 0
        res_list = [1]
        # res = 2^x * 3^y * 5^z
        x = 0
        y = 0
        z = 0
        for i in range(1, index):
            next2 = res_list[x] * 2
            next3 = res_list[y] * 3
            next5 = res_list[z] * 5
            res_list.append(min(next2, next3, next5))
            if res_list[i] == next2: x += 1
            if res_list[i] == next3: y += 1
            if res_list[i] == next5: z += 1
        return res_list[index-1]

print(Solution().GetUglyNumber_Solution(4))
