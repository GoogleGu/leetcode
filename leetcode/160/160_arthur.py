# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode_destructive(self, headA, headB):
        """ 破坏原链表结构，O(N)时间复杂度，O(1)空间复杂度 """

        current_node = headA
        temp_node = None
        while current_node is not None:
            temp_node = current_node.next
            current_node.next = headB
            current_node = temp_node
        
        current_node = headB
        while current_node is not None:
            if current_node.next is headB:
                return current_node
            current_node = current_node.next

        return None

    def getIntersectionNode(self, headA, headB):
        """ T=O(N), S=O(1) """

        node_1, node_2 = headA, headB
        while node_1 and node_2:
            node_1 = node_1.next
            node_2 = node_2.next
        
        if node_1:
            node_2 = headA
        else:
            node_1 = headB
        
        while node_1 and node_2:
            node_1 = node_1.next
            node_2 = node_2.next 
        
        if node_1:
            node_2 = headA
        else:
            node_1 = headB
        
        while node_1 and node_2:
            if node_1 is node_2:
                return node_1
            node_1 = node_1.next
            node_2 = node_2.next
        return None
