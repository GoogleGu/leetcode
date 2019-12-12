# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # 无法处理循环链表
    def reverseList(self, head: ListNode) -> ListNode:
        if head.next:
            node = self.reverseList(head.next)
        
        node = ListNode(head.val)
        node.next = self.reverseList(head.next)


    def recursion(self, head: ListNode) -> ListNode:
        pass
