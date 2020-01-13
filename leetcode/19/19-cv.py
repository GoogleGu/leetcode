# -*- coding:utf-8 -*-

# 题目url: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
# 描述：给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        n_ = 0
        while n_ <= n:
            fast = fast.next
            n_ += 1
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
res = Solution().removeNthFromEnd(head, 2)
print(res)
res = Solution().removeNthFromEnd(ListNode(1), 1)
print(res)