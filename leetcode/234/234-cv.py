# -*- coding:utf-8 -*-

# 题目url: https://leetcode-cn.com/problems/palindrome-linked-list/
# 描述：请判断一个链表是否为回文链表。
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # 修改原链表
    def isPalindrome(self, head):
        fast = head
        slow = head
        pre = None
        prepre = None
        # 先找到中心位置, 同时翻转前半段链表
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
            pre.next = prepre
            prepre = pre
        if fast:
            slow = slow.next
        while slow and pre:
            if slow.val != pre.val:
                return False
            slow = slow.next
            pre = pre.next
        
        return True
    

head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)
# head.next.next.next = ListNode(1)
res = Solution().isPalindrome(head)
print(res)
