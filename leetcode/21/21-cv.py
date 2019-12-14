# -*- coding:utf-8 -*-

# 题目url: https://leetcode-cn.com/problems/merge-two-sorted-lists/
# 描述：将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # 为实现 空间复杂的为 O(1), 采用迭代法 
    #   将l2的元素全部有序加入l1
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next, l1 = l1, l1.next
            else:
                prev.next, l2 = l2, l2.next
            prev = prev.next

        prev.next = l1 if l1 else l2
        return prehead.next



