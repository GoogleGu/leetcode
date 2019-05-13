# -*- coding:utf-8 -*-
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同

二叉搜索树
若它的左子树非空，则左子树上所有记录的关键字均小于根记录的值。
若它的右子树非空，则右子树上所有记录的关键字均大于根记录的值。
左、右子树本身又各是一棵二叉排序树。

思路：最后一个值是根节点
将序列除了最后一个节点 ，分成两部分，
并且前部分比 根节点 小，后部分比 根节点 大，就是二叉排序的后序了；否则就不是。
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) > 0:
            if self.valid(sequence):
                return "true"
        return "false"

    def valid(self, node):
        if len(node) > 0:
            end = len(node) - 1
            start = 0
            # 定位右节点
            while node[start] < node[end]:
                start += 1
            if start != end:
                left_node = node[0:start]
                right_node = node[start:end]
                if node[end] < min(right_node):
                    return self.valid(left_node) and self.valid(right_node)
                return False
        return True
