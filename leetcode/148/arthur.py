"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

"""
from queue import PriorityQueue


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         end_node = None
#         while end_node is not head:
#             end_node = self._pop_up(None, head, end_node)
#         return head

#     def _pop_up(self, last_node, current_node, end_node) -> ListNode:
#         if last_node and current_node.val < last_node.val:
#             current_node.val, last_node.val = last_node.val, current_node.val
#         if current_node.next is not end_node:
#             return self.pop_up(current_node, current_node.next, end_node)
#         else:
#             return current_node


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        ptr = head
        p_queue = PriorityQueue()
        while ptr != None:
            p_queue.put(ptr.val)
            ptr = ptr.next
        ptr = head
        while not p_queue.empty():
            ptr.val = p_queue.get()
            ptr = ptr.next
        return head