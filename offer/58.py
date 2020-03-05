# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        
        if pRoot is None:
            return True

        return self.compare_nodes(pRoot.left, pRoot.right)

    def compare_nodes(self, node1, node2):
        if node1 is None or node2 is None: 
            return node1 is None and node2 is None
        if node1.val != node2.val: 
            return False
        
        return self.compare_nodes(node1.left, node2.right) and self.compare_nodes(node1.right, node2.left)


if __name__ == "__main__":
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.right = TreeNode(6)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(7)

    result = Solution().isSymmetrical(root)
    print(result)