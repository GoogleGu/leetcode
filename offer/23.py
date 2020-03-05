# -*- coding:utf-8 -*-
class Solution:

    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False

        return self.is_sequence_of_bst(sequence, 0, len(sequence))

    def is_sequence_of_bst(self, sequence, start, end):
        if start == end:
            return True
            # 找到根节点_对应index
        root_index = end-1

        # 找到理论上的左右树分界点
        first_index_of_right_sub_tree = start
        while first_index_of_right_sub_tree < root_index:
            if sequence[first_index_of_right_sub_tree] < sequence[root_index]:
                first_index_of_right_sub_tree += 1
            else:
                break

        # 找到左右树对应的起始点
        left_tree_start = start
        left_tree_end = first_index_of_right_sub_tree
        right_tree_start = first_index_of_right_sub_tree
        right_tree_end = root_index

        # 如果右树里有比根小的即为假，否则继续递归判断左右子树
        if any(sequence[i] < sequence[root_index] for i in range(right_tree_start, right_tree_end)):
            return False
        else:
            return self.is_sequence_of_bst(sequence, left_tree_start, left_tree_end) \
                   and self.is_sequence_of_bst(sequence, right_tree_start, right_tree_end)


if __name__ == '__main__':
    seq = [4,8,6,12,16,14,10]
    print(Solution().VerifySquenceOfBST(seq))
