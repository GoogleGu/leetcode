# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        lists = [head for head in lists if head]
        if not lists:
            return lists
        head = new_node = self.get_smallest_head(lists)

        while lists:
            new_node.next = self.get_smallest_head(lists)
            new_node = new_node.next
        return head

    def get_smallest_head(self, lists):
        min_val = lists[0].val
        smallest_index = 0

        for i in range(len(lists)):
            if lists[i].val < min_val:
                min_val = lists[i].val
                smallest_index = i
        node = lists[smallest_index]
        lists[smallest_index] = node.next
        if lists[smallest_index] is None:
            del lists[smallest_index]
        return node
