
# -*- coding:utf-8 -*-

# 题目描述
# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 is None or pRoot2 is None:
            return False
        result = False
        if pRoot1.val == pRoot2.val:
            # 根节点相同
            result = self.handle_item(pRoot1, pRoot2)
        if not result:
            # 遍历左树
            result = self.handle_item(pRoot1.left, pRoot2)
        if not result:
            # 遍历右树
            result = self.handle_item(pRoot1.right, pRoot2)
        return result

    def handle_item(self, root1, root2):
        # 判断该节点是否相同
        if root2 is None:
            # 子树 已经遍历完，
            return True
        if root1 is None:
            # 母树已经遍历完，子树还没有遍历完，说明不属于
            return False
        if root1.val is not root2.val:
            return False
        # 比较左树是否相同
        left_result = self.handle_item(root1.left, root2.left)
        # 比较右树是否相同
        right_result = self.handle_item(root1.right, root2.right)
        return left_result and right_result
