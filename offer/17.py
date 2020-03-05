# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 is None or pRoot2 is None:
            return False
        elif self.are_same_trees(pRoot1, pRoot2):
            return True
        else:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def are_same_trees(self, root1, root2):
        if root2 is None:
            return True
        elif root1 and root1.val == root2.val:
            return self.are_same_trees(root1.left, root2.left) and self.are_same_trees(root1.right, root2.right)
        else:
            return False
