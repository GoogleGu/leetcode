# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> ListNode:
        slow_node = head
        fast_node = head

        while True:
            try:
                fast_node = fast_node.next.next
            except AttributeError:
                return False
            slow_node = slow_node.next

            if fast_node is slow_node:
                return True