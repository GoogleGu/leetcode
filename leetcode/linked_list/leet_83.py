# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        elements = set()
        fake_head = ListNode(None)
        fake_head.next = head
        prev = fake_head
        this = head
        while head:
            if head.val in elements:
                prev.next = head.next
            else:
                elements.add(head.val)
                prev = prev.next
            head = head.next

        return fake_head.next
