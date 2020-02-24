# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        node1, node2 = l1, l2
        null_node = ListNode(0)
        last_node = null_node
        place_holder = 0
        while node1 and node2:
            this_num = node1.val + node2.val + place_holder
            last_node.next = ListNode(this_num % 10)
            last_node = last_node.next
            place_holder = this_num // 10
            node1, node2 = node1.next, node2.next

        longer_list = node1 or node2
        while longer_list:
            this_num = longer_list.val + place_holder
            last_node.next = ListNode(this_num % 10)
            last_node = last_node.next
            place_holder = this_num // 10
            longer_list = longer_list.next
        if place_holder > 0:
            last_node.next = ListNode(1)

        return null_node.next
