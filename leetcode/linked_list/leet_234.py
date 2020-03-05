# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        # 找到链表中点
        slow_node = head
        fast_node = head
        while fast_node:
            slow_node = slow_node.next
            if fast_node.next:
                fast_node = fast_node.next.next
            else:
                break

        # 反转链表
        prev_node = None
        while slow_node.next:
            temp = slow_node.next
            slow_node.next = prev_node
            prev_node = slow_node
            slow_node = temp
        slow_node.next = prev_node

        # 比较是否回文
        forward_node, backward_node = head, slow_node
        while backward_node:
            if forward_node.val != backward_node.val:
                return False
            backward_node = backward_node.next
            forward_node = forward_node.next
        return True


