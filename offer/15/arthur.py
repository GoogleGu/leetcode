# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode

    def ReverseList(self, pHead):
        curr_node = None
        next_node = pHead

        while next_node:
            # 保存下下个节点信息
            next_of_next = next_node.next
            # 将下个节点的指针指向当前节点
            next_node.next = curr_node

            # 向前移动节点
            curr_node = next_node
            next_node = next_of_next
        return curr_node


if __name__ == '__main__':
    head = ListNode(x=1)
    head.next = ListNode(x=2)
    head.next.next = ListNode(x=3)

    solution = Solution()
    reversed_head = solution.ReverseList(head)
    curr_node = reversed_head
    while curr_node:
        print(curr_node.val)
        curr_node = curr_node.next
