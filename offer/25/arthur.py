# -*- coding:utf-8 -*-
class RandomListNode:

    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
        self.index = None


class Solution:
    # 返回 RandomListNode

    original_nodes = {}
    copied_nodes = {}

    def Clone(self, pHead):
        if not pHead:
            return
        self.original_nodes = {}
        self.copied_nodes = {}
        head = self.clone_next(pHead)
        self.clone_random(pHead, head)
        return head

    def clone_next(self, source_head):
        """ 沿着next指针遍历链表，复制链表节点和next指针 """
        if not source_head:
            return
        index = id(source_head)
        self.original_nodes[index] = source_head
        head = source_head.copy()
        self.copied_nodes[index] = head
        head.next = self.clone_next(source_head.next)
        return head

    def clone_random(self, source_head, copied_head):
        """ 沿着next指针遍历链表，复制random指针 """
        if not source_head:
            return
        if source_head.random:
            index = id(source_head.random)
            if self.original_nodes.get(index):
                copied_head.random = self.copied_nodes[index]
            else:
                self.original_nodes[index] = source_head
                copied_head.random = source_head.copy()
        self.clone_random(source_head.next, copied_head.next)

