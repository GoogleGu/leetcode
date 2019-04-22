# -*- coding:utf-8 -*-
class Solution:

    stack = []
    minimum = None

    def push(self, node):
        self.stack.append(node)
        if self.minimum is None or node < self.minimum:
            self.minimum = node
        # write code here

    def pop(self):
        if self.stack:
            top_element = self.stack.pop(-1)
            if top_element == self.minimum:
                self.minimum = min(self.stack)

        # write code here
    def top(self):
        if self.stack:
            return self.stack[-1]
        # write code here

    def min(self):
        return self.minimum
        # write code here