# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        return self.get_next(pNode, pNode)
    
    def get_next(self, node, source_node):
        if node is None or source_node is None:
            return None
        if source_node == node:
            next_node = self.get_next_mid_order_node(node.right)
        elif source_node == node.left:
            next_node = node
        else:
            next_node = self.get_next(node.next, node)
        
        if next_node is None:
            return self.get_next(node.next, node)
        else:
            return next_node


    def get_next_mid_order_node(self, pNode):

        if pNode is None:
            return None
        
        return self.get_next_mid_order_node(pNode.left) or pNode


        