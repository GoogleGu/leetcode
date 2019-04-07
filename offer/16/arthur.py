# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):

        p_curr_1 = pHead1
        p_curr_2 = pHead2

        null_head = ListNode(x=-1000000)
        new_curr = null_head

        while p_curr_1 and p_curr_2:
            if p_curr_1.val < p_curr_2.val:
                new_curr.next = p_curr_1
                p_curr_1 = p_curr_1.next
            else:
                new_curr.next = p_curr_2
                p_curr_2 = p_curr_2.next
            new_curr = new_curr.next

        if p_curr_1:
            new_curr.next = p_curr_1
        else:
            new_curr.next = p_curr_2
        return null_head.next