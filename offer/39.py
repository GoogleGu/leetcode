# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    is_balanced = True

    def IsBalanced_Solution(self, pRoot):
        self.is_balanced = True
        self.find_depth(pRoot, 0)
        return self.is_balanced

    def find_depth(self, root, depth):
        if not root:
            return depth

        depth += 1

        left_depth = self.find_depth(root.left, depth)
        right_depth = self.find_depth(root.right, depth)
        if abs(left_depth - right_depth) > 1:
            self.is_balanced = False
        return max(left_depth, right_depth)
