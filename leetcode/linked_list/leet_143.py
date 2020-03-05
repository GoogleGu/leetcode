# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        # 找到中点
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        front_node = head
        tail_node = slow.next
        slow.next = None
        tail_node = self.reverseList(tail_node)


        while tail_node:
            front_next, tail_next = front_node.next, tail_node.next
            front_node.next = tail_node
            tail_node.next = front_next
            front_node, tail_node = front_next, tail_next

        return head



    def reverseList(self, head):
        if not head:
            return None
        return self._iterative(head)

    @staticmethod
    def _iterative(head):
        last = None
        while head is not None:
            next_node = head.next
            head.next = last
            last, head = head, next_node
        return last
