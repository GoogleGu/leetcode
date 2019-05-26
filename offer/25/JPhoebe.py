# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    def Clone(self, pHead):
        if not pHead:
            return
        new_node = RandomListNode(pHead.label)
        new_node.random = pHead.random
        new_node.next = self.Clone(pHead.next)
        return new_node
