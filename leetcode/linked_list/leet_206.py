"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # return self._iterative(head)
        if not head:
            return None
        return self._recursive(None, head)

    @staticmethod
    def _iterative(head):
        last = None
        while head is not None:
            next_node = head.next
            head.next = last
            last, head = head, next_node
        return last

    def _recursive(self, last, current):
        next_node = current.next
        current.next = last
        if next_node:
            return self._recursive(current, next_node)
        else:
            return current           
        