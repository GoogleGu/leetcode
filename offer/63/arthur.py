# -*- coding:utf-8 -*-
class TreeNode:

    def __init__(self, val, count=1):
        self.val = val
        self.left = None
        self.right = None
        self.count = count

class Solution:

    def __init__(self):
        self.tree = AVLTree()

    def Insert(self, num):
        self.tree.insert(None, self.tree.root, num)

    def GetMedian(self, dummy=None):
        left_count = get_count(self.tree.root.left)
        right_count = get_count(self.tree.root.right)
        if left_count == right_count:
            return self.tree.root.val
        else:
            tmp = None
            if left_count > right_count:
                tmp = self.tree.root.left
                while tmp.right is not None:
                    tmp = tmp.right
            else:
                tmp = self.tree.root.right
                while tmp.left is not None:
                    tmp = tmp.left
            return (self.tree.root.val + tmp.val) / 2
 

class AVLTree:

    def __init__(self):
        self.root = None

    def insert(self, root_parent, root, val):
        if root is None:
            self.root = TreeNode(val)
        
        elif root.val >= val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insert(root, root.left, val)
            root.count = get_count(root.left) + get_count(root.right) + 1
            if get_count(root.left) - get_count(root.right) == 2:
                if val < root.left.val:
                    self.rotate_ll(root_parent, root)
                else:
                    self.rotate_lr(root_parent, root)
        else:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insert(root, root.right, val)
            root.count = get_count(root.left) + get_count(root.right) + 1
            if get_count(root.right) - get_count(root.left) == 2:
                if val > root.right.val:
                    self.rotate_rr(root_parent, root)
                else:
                    self.rotate_rl(root_parent, root)

    def rotate_ll(self, t_parent, t):
        k = t.left
        tm = None
        while k.right is not None:
            k.count -= 1
            tm = k
            k = k.right
        if k != t.left:
            k.left = t.left
            tm.right = None
        t.left = None
        k.right = t

        t.count = get_count(t.left) + get_count(t.right) + 1
        k.count = get_count(k.left) + t.count + 1
        
        if t_parent is None:
            self.root = k
        elif t_parent.left == t:
            t_parent.left = k
        else:
            t_parent.right == k


    def rotate_rr(self, t_parent, t):
        k = t.right
        tm = None
        while k.left is not None:
            k.count -= 1
            tm = k
            k = k .left
        if k != t.right:
            k.right = t.right
            tm.left = None
        t.right = None
        k.left = t
        
        t.count = get_count(t.left) + 1
        k.count = get_count(k.right) + t.count + 1

        if t_parent is None:
            self.root = k
        elif t_parent.left == t:
            t_parent.left = k
        else:
            t_parent.right == k


    def rotate_lr(self, t_parent, t):
        self.rotate_rr(t, t.left)
        self.rotate_ll(t_parent, t)


    def rotate_rl(self, t_parent, t):
        self.rotate_ll(t, t.right)
        self.rotate_rr(t_parent, t)


def get_count(node):
    if node is None:
        return 0
    else:
        return node.count


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


# --------------------------------------------------------------------------- #




 
class SolutionHeap:
    def __init__(self):
        self.minNums=[]
        self.maxNums=[]
 
    def maxHeapInsert(self,num):
        self.maxNums.append(num)
        lens = len(self.maxNums)
        i = lens - 1
        while i > 0:
            if self.maxNums[i] > self.maxNums[(i - 1) / 2]:
                t = self.maxNums[(i - 1) / 2]
                self.maxNums[(i - 1) / 2] = self.maxNums[i]
                self.maxNums[i] = t
                i = (i - 1) / 2
            else:
                break
 
    def maxHeapPop(self):
        t = self.maxNums[0]
        self.maxNums[0] = self.maxNums[-1]
        self.maxNums.pop()
        lens = len(self.maxNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.maxNums[nexti + 1] > self.maxNums[nexti]:
                nexti += 1
            if self.maxNums[nexti] > self.maxNums[i]:
                tmp = self.maxNums[i]
                self.maxNums[i] = self.maxNums[nexti]
                self.maxNums[nexti] = tmp
                i = nexti
            else:
                break
        return  t
 
    def minHeapInsert(self,num):
        self.minNums.append(num)
        lens = len(self.minNums)
        i = lens - 1
        while i > 0:
            if self.minNums[i] < self.minNums[(i - 1) / 2]:
                t = self.minNums[(i - 1) / 2]
                self.minNums[(i - 1) / 2] = self.minNums[i]
                self.minNums[i] = t
                i = (i - 1) / 2
            else:
                break
 
    def minHeapPop(self):
        t = self.minNums[0]
        self.minNums[0] = self.minNums[-1]
        self.minNums.pop()
        lens = len(self.minNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.minNums[nexti + 1] < self.minNums[nexti]:
                nexti += 1
            if self.minNums[nexti] < self.minNums[i]:
                tmp = self.minNums[i]
                self.minNums[i] = self.minNums[nexti]
                self.minNums[nexti] = tmp
                i = nexti
            else:
                break
        return t
 
    def Insert(self, num):
        if (len(self.minNums)+len(self.maxNums))&1==0:
            if len(self.maxNums)>0 and num < self.maxNums[0]:
                self.maxHeapInsert(num)
                num = self.maxHeapPop()
            self.minHeapInsert(num)
        else:
            if len(self.minNums)>0 and num > self.minNums[0]:
                self.minHeapInsert(num)
                num = self.minHeapPop()
            self.maxHeapInsert(num)
 
    def GetMedian(self,n=None):
        allLen = len(self.minNums) + len(self.maxNums)
        if allLen ==0:
            return -1
        if allLen &1==1:
            return self.minNums[0]
        else:
            return (self.maxNums[0] + self.minNums[0]+0.0)/2