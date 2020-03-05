# -*- coding:utf-8 -*-

""" 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。 """

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    node_list = []

    def Convert(self, pRootOfTree):
        self.node_list = []
        if pRootOfTree:
            self.scan_tree(pRootOfTree)
            self.change_pointers()
        return self.node_list[0] if self.node_list else None

    def scan_tree(self, root):
        """ 扫描当前树，将其按中序遍历顺序添加到node list列表中 """
        if root.left:
            self.scan_tree(root.left)
        self.node_list.append(root)
        if root.right:
            self.scan_tree(root.right)

    def change_pointers(self):
        """ 调整指针指向 """
        nodes = [None]
        nodes.extend(self.node_list)
        nodes.append(None)
        for last, this, next in zip(nodes[:-2], nodes[1:-1], nodes[2:]):
            this.left = last
            this.right = next
