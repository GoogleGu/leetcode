
# -*- coding:utf-8 -*-
# 
"""
题目url: https://leetcode-cn.com/problems/add-two-numbers/
描述：
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    # 维护一个进位数即可
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        r = res
        add = 0
        while l1 or l2:
            x, y = 0, 0
            if l1:
                x, l1 = l1.val, l1.next
            if l2:
                y, l2 = l2.val, l2.next
            add = x + y + add
            r.next = ListNode(add % 10) 
            add = add // 10
            r = r.next
        if add > 0:
            r.next = ListNode(add)
        return res.next