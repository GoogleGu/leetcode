# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        fake_head = ListNode(None)
        fake_head.next = head

        node = fake_head
        while node and node.next and node.next.next:
            node_1 = node
            node_2 = node.next
            node_3 = node.next.next
            node_4 = node.next.next.next
            node_1.next = node_3
            node_2.next = node_4
            node_3.next = node_2
            node = node_2
        return fake_head.next



