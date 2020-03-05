# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode

    counter = 0

    def KthNode(self, pRoot, k):
        self.counter = 0
        return self.find_kth_iter(pRoot, k)

    
    def find_kth_iter(self, node, k):
        if node is None:
            return None

        result = None

        if node.left:
            result = self.find_kth_iter(node.left, k)

        self.counter += 1
        if self.counter == k:
            return node

        if node.right and result is None:
            result = self.find_kth_iter(node.right, k)
        return result


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(Solution().KthNode(root, 3).val)
