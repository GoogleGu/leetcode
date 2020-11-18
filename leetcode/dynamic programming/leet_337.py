# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def sub_rob(node):
            if not node: 
                return 0, 0
            rob_left, skip_left = sub_rob(node.left)
            rob_right, skip_right = sub_rob(node.right)
            rob_this = node.val + skip_left + skip_right
            skip_this = max(rob_left, skip_left) + max(rob_right, skip_right)
            return rob_this, skip_this

        return max(sub_rob(root))