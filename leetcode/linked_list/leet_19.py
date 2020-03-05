# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        fast_node = head
        slow_node = head

        while n > 0:
            fast_node = fast_node.next
            n -= 1

        if not fast_node:
            return head.next

        while fast_node.next:
            fast_node = fast_node.next
            slow_node = slow_node.next


        slow_node.next = slow_node.next.next
        return head
