# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        count = 0
        fake_head = ListNode(None)
        fake_head.next = head
        node = fake_head
        while count <= n:
            next_node = node.next
            if count == m-1:
                cut_end_1 = node
            elif count == m:
                cut_end_2 = node
                temp_node = node
            elif m < count <= n:
                node.next = temp_node
                temp_node = node
            if count == n:
                cut_end_1.next = node
                cut_end_2.next = next_node
            count += 1
            node = next_node
        return fake_head.next
