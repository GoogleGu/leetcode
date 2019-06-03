"""
输入一棵二叉搜索树，
将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree:
            return pRootOfTree

        # 遍历左子树, 获取排序后的左子树的head
        new_left = self.Convert(pRootOfTree.left)
        # new_left的最后一个节点last_left
        last_left = new_left
        while last_left and last_left.right:
            last_left = last_left.right
        # 与当前根节点排序
        if new_left:
            last_left.right = pRootOfTree
            pRootOfTree.left = last_left

        # 遍历右子树
        new_right = self.Convert(pRootOfTree.right)
        # 与当前根节点排序
        if new_right:
            new_right.left = pRootOfTree
            pRootOfTree.right = new_right

        # 返回最终结果
        return new_left if new_left else pRootOfTree
