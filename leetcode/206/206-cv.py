# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # 无法处理循环链表
    def reverseList(self, head):
        # 拿到最后的元素
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node

    # 多元赋值
    def reverseList2(self, head):
        res = None
        while head:
            res, res.next, head = head, res, head.next
        return res

