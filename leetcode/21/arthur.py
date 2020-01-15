# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not (l1 and l2):
            return l1 or l2

        if l1.val > l2.val:
            new_node = l2
            l2 = l2.next
        else:
            new_node = l1
            l1 = l1.next
        head = new_node


        while l1 and l2:
            if l1.val > l2.val:
                new_node.next = l2
                l2 = l2.next
            else:
                new_node.next = l1
                l1 = l1.next
            new_node = new_node.next

        new_node.next = l1 or l2
        return head


