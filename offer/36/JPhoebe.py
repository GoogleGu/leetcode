# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        head1_list = []
        head2_list = []
        while pHead1:
            head1_list.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            head2_list.append(pHead2)
            pHead2 = pHead2.next
        last_index = -1
        while True:
            head1_length = len(head1_list)
            head2_length = len(head2_list)
            head1 = head1_list[last_index]
            head2 = head2_list[last_index]
            if head1.val != head2.val and last_index == -1:
                return None
            if head1.val != head2.val:
                return head1_list[last_index+1]
            if -last_index==head1_length or -last_index==head2_length:
                if head1.val == head2.val:
                    return head1
                return None
            last_index -= 1


head1 = ListNode(8, ListNode(7, ListNode(5, ListNode(6, None))))
head2 = ListNode(1, ListNode(8, ListNode(7, ListNode(5, ListNode(6, None)))))
print (Solution().FindFirstCommonNode(head1, head2))
