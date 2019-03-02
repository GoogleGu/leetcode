# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]

    @staticmethod
    def print_list_from_tail_to_head(listNode):
        """
        运行时间：25ms
        占用内存：5624k
        """
        reversed_list = []
        current_node = listNode
        while current_node:
            reversed_list.insert(0, current_node.val)
            current_node = current_node.next
        return reversed_list

