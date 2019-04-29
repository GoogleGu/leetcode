# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        temp_popV = popV.copy()
        index = 0
        for element in pushV:
            # 如果比较当前位置元素不相等，在当前位置将列表反转
            if element != temp_popV[index]:
                temp_popV = temp_popV[index:][::-1]
                index = 0
                if element != temp_popV[index]:
                    return False
            index += 1
        return True


if __name__ == '__main__':
    push = [1, 2, 3, 4, 5]
    pop = [3,5,4,2,1]
    print(Solution().IsPopOrder(push, pop))