# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def re_construct_binary_tree(self, pre, tin):
        """
        返回构造的TreeNode根节点
        运行时间：88ms
        占用内存：5800k
        """
        #  边界情况：前序遍历为空，返回None
        if not pre:
            return None

        # 根节点一定是前序的首个值
        root_val = pre[0]
        # 中序中根节点的左边为左子树的中序遍历结果，右边同理
        root_node_tin_index = tin.index(root_val)
        left_tin = sub_list(tin, end=root_node_tin_index)
        right_tin = sub_list(tin, start=root_node_tin_index+1)
        # 前序结果中根节点后是前序左树加上前序右树顺序排列
        left_pre = sub_list(pre, start=1, end=1+len(left_tin))
        right_pre = sub_list(pre, start=len(left_pre)+1)

        # 构造当前节点，并将构造左右子树的任务进行递归
        current_node = TreeNode(root_val)
        current_node.left = self.re_construct_binary_tree(left_pre, left_tin)
        current_node.right = self.re_construct_binary_tree(right_pre, right_tin)

        return current_node


def sub_list(parent_list, start=None, end=None):
    try:
        if start is not None and end is not None:
            return parent_list[start:end]
        elif start is not None and end is None:
            return parent_list[start:]
        elif start is None and end is not None:
            return parent_list[:end]
        elif start is None and end is None:
            return parent_list
    except IndexError:
        return []
