# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:

    res = True

    def IsBalanced_Solution(self, pRoot):
        self.TreeDepth(pRoot)
        return self.res


    def TreeDepth(self, pRoot):
        if not self.res:
            return 0
        if not pRoot:
            return 0
        else:
            left = self.TreeDepth(pRoot.left)
            right = self.TreeDepth(pRoot.right)
            if (math.fabs(left - right) > 1):
                self.res = False
            return 1 + left if left > right else 1 + right

