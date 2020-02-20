# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        length = 1
        tail_node = head
        while head.next:
            length += 1
            tail_node = tail_node.next

        count = -1
        new_tail = head
        while count != k:
            count += 1
            new_tail = new_tail.next

        tail_node.next = head
        new_head = new_tail.next
        new_tail.next = None
        return new_head
