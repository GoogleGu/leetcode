# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def FindFirstCommonNode(self, pHead1, pHead2):

        sequence = set()

        current_head = pHead1
        while current_head:
            sequence.add(id(current_head))
            current_head = current_head.next

        current_head = pHead2
        while current_head:
            if id(current_head) in sequence:
                return current_head
            current_head = current_head.next

        return None
