# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]

    breath_first_result = []

    def PrintFromTopToBottom(self, root):
        self.breath_first_result = []
        if root:
            self.process_node(root, level=1)
        self.breath_first_result.sort(key=lambda x: x[0])
        return [element[1] for element in self.breath_first_result]

    def process_node(self, node, level):
        self.breath_first_result.append((level, node.val))
        if node.left:
            self.process_node(node.left, level+1)
        if node.right:
            self.process_node(node.right, level+1)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node1.left = TreeNode(2)
    node1.right = TreeNode(3)
    result = Solution().PrintFromTopToBottom(node1)
    print(result)