# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head):
        slow_node = head
        fast_node = head

        while True:
            try:
                fast_node = fast_node.next.next
            except AttributeError:
                return None
            slow_node = slow_node.next
            if fast_node is slow_node:
                break

        fast_node = head
        while fast_node is not slow_node:
            fast_node = fast_node.next
            slow_node = slow_node.next
        
        return slow_node
