# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        self.stream = []

    def Insert(self, num):
        # 二分插入
        return

    def GetMedian(self):
        n = len(self.stream)
        if n % 2 == 0:
            return (self.stream[n//2] + self.stream[n//2 - 1]) / 2
        else:
            return self.stream[n//2]

class TreeNode:

    def __init__(self, val, height=1):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.height = height
    
    def find(self, val):
        if self.val == val:
            return self
        elif self.val > val:
            if self.left is None:
                return None
            return self.find(self.left)
        else:
            if self.right is None:
                return None
            return self.find(self.right)
    
    def insert(self, node):

        if self.val > node.val:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)
        update_height(self)
    
    def __str__(self):
        return '{}'.format(self.val)

def height(node):
    if node is None:
        return 0    
    else:
        return node.height

def update_height(node):
    extra = 0
    if node.left is not None:
        extra += 1
    if node.right is not None:
        extra += 1
    node.height = height(node.left) + height(node.right) + extra

class AVLTree:
    """
    只实现了插入的自平衡，没有实现删除方法和相应的自平衡。
    """

    def __init__(self):
        self.root = None
        self.node_nums = 0
    
    def find(self, val):
        if not self.root:
            return None
        else:
            return self.root.find(val)

    def insert(self, val):
        self.node_nums += 1
        new_node = TreeNode(val)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)
        self.rebalance(new_node)

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) - height(node.right) > 1:
                self.right_rotate(node)
            elif height(node.left) - height(node.right) < -1:
                self.left_rotate(node)
            node = node.parent

    def right_rotate(self, x_node):
        """
        右旋有两种情况：
            - x.left.right是空，这种情况下和正常avl的右旋方式相同
            - x.left.right不是空，这种情况下旋转后x.left.right取代原来x的位置成为当前子树的根节点
        """
        root = x_node.parent
        l_node = x_node.left
        lr_node = l_node.right

        if lr_node is None:
            # 正常情况: x.left.right是空
            sub_root = l_node

            x_node.left = lr_node
            x_node.parent = l_node

            l_node.right = x_node
            l_node.parent = root
        else:
            # 异常情况：x.left.right不是空
            sub_root = lr_node

            l_node.right = None
            l_node.parent = lr_node

            x_node.parent = lr_node
            x_node.left = None

            lr_node.left = l_node            
            lr_node.right = x_node
            lr_node.parent = root

        if root is None:
            self.root = sub_root
        else:
            if root.left is x_node:
                root.left = sub_root
            else:
                root.right = sub_root
        update_height(x_node)
        update_height(sub_root)

    def left_rotate(self, x_node):
        """
        左旋同右旋
        """
        root = x_node.parent
        r_node = x_node.right
        rl_node = r_node.left

        x_node.right = rl_node
        if rl_node is not None:
            rl_node.parent = x_node

        r_node.left = x_node
        x_node.parent = r_node

        r_node.parent = root
        if root is None:
            self.root = r_node
        else:
            if self.root.left is x_node:
                self.root.left = r_node
            else:
                self.root.right = r_node
        
        update_height(x_node)
        update_height(r_node)


def print_tree(root):

    if root is None:
        return []

    nodes = [[root]]

    while True:
        last_row = nodes[-1]
        this_row = []
        for node in last_row:
            if node.left:
                this_row.append(node.left)
            if node.right:
                this_row.append(node.right)
        if len(this_row) == 0:
            break
        else:
            nodes.append(this_row)
    
    result = []
    for row in nodes:
        result.append([node.val for node in row])
    
    return result

if __name__ == "__main__":
    avl = AVLTree()
    avl.insert(5)
    avl.insert(4)
    avl.insert(3)
    avl.insert(2)
    avl.insert(1)
    avl.insert(0)
    avl.insert(-1)
    print(print_tree(avl.root))