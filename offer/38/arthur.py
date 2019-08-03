# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def TreeDepth(self, pRoot):
        return self.find_depth(pRoot, 0)

    def find_depth(self, root, depth):
        if not root:
            return depth

        depth += 1

        left_depth = self.find_depth(root.left, depth)
        right_depth = self.find_depth(root.right, depth)
        return max(left_depth, right_depth)
