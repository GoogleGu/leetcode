# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        this_node = pHead
        ids = set()

        while True:
            if not this_node:
                return None
            this_id = id(this_node)
            if this_id in ids:
                return this_node
            else:
                ids.add(this_id)
            this_node = this_node.next