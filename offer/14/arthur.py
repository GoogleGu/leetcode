# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        if not head or k <= 0:
            return None
        temp_list = []
        node = head
        while True:
            temp_list.append(node)
            if node.next:
                node = node.next
            else:
                break
        if k > len(temp_list):
            return None
        return temp_list[-k]
