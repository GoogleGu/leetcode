# -*- coding:utf-8 -*-

# 题目描述
# 操作给定的二叉树，将其变换为源二叉树的镜像。
# 输入描述:
# 二叉树的镜像定义：源二叉树
# 8
# / \
#     6   10
# / \  / \
#     5  7 9 11
# 镜像二叉树
# 8
# / \
#     10   6
# / \  / \
#     11 9 7  5

class Solution:
    def Mirror(self, root):
        # 递归更换左右节点
        self.hand_mirror(root)
        return root

    def hand_mirror(self, root):
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.hand_mirror(root.left)
        self.hand_mirror(root.right)
