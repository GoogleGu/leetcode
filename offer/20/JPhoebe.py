"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""

class Solution:
    stack = []
    min_list = []

    def push(self, node):
        # 每次压入数据栈数据与最小数据进行比较，yes: 存入数据栈、辅助栈
        self.stack.append(node)
        if len(self.min_list) < 1:
            self.min_list.append(node)
        else:
            if self.min_list[-1] > node:
                self.min_list.append(node)

    def pop(self):
        if self.stack is None:
            return None
        if self.stack[-1] == self.min_list[-1]:
            self.min_list.pop()
        value = self.stack.pop()
        return value

    def top(self):
        if self.stack is None:
            return None
        value = self.stack[-1]
        return value

    def min(self):
        if self.min_list is None:
            return None
        value = self.min_list[-1]
        return value

