# -*- coding:utf-8 -*-

# 题目url: https://leetcode-cn.com/problems/merge-k-sorted-lists/
# 描述：合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
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

    def mergeKLists(self, lists):
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None


res = Solution().mergeKLists([])
print(res)


