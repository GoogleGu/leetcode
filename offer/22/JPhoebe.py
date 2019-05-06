"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []
        result = []
        node_sort_list = [root]
        for node in node_sort_list:
            result.append(node.val)
            # 二叉树 -> sortList
            if node.left is not None:
                node_sort_list.append(node.left)
            if node.right is not None:
                node_sort_list.append(node.right)
        return result
