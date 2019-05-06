"""
输入两个整数序列，第一个序列表示栈的压入顺序，
请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""

class Solution:
    def IsPopOrder(self, pushV, popV):
        # 模拟出栈
        data_result = []
        pop_index = 0
        for push_value in pushV:
            data_result.append(push_value)
            if push_value == popV[pop_index]:
                data_result.remove(push_value)
                pop_index += 1
        # 剩余数出栈
        for pop_index in range(pop_index, len(popV)):
            if data_result[len(data_result)-1] == popV[pop_index]:
                data_result.pop()
                pop_index += 1
        if data_result:
            return False
        return True

Solution().IsPopOrder([1,2,3,4,5], [4,5,3,2,1])
