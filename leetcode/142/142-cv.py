# -*- coding:utf-8 -*-

# 题目url: https://leetcode-cn.com/problems/linked-list-cycle-ii/
# 描述：
#   给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#   为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#   说明：不允许修改给定的链表。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        meet = self.meetCycle(head)
        if meet:
            c = head
            while c != meet:
                c = c.next 
                meet = meet.next
        return meet
    
    def meetCycle(self, head):
        if not head or not head.next:
            return None
        a, b = head, head
        while a and b and b.next:
            a, b = a.next, b.next.next
            if a == b:
                return a
        return None


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
res = Solution().detectCycle(head)
print(res)