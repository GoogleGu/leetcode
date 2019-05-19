"""
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径

    solution = []

    def FindPath(self, root, expectNumber):

        def find_path_of_expected_number(root, path, expect_num):
            if not root:
                return

            expect_num -= root.val
            path.append(root.val)

            if expect_num == 0 and not root.left and not root.right:
                self.solution.append(path)
            else:
                find_path_of_expected_number(root.left, path.copy(), expect_num)
                find_path_of_expected_number(root.right, path.copy(), expect_num)

        self.solution = []
        find_path_of_expected_number(root, [], expectNumber)
        self.solution.sort(key=lambda x: len(x), reverse=True)
        return self.solution


if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(10)
    r1.right = TreeNode(12)
    r1.left = TreeNode(5)
    r1.left.left = TreeNode(4)
    r1.left.right = TreeNode(7)
    res = s.FindPath(r1, 22)
    print(res)