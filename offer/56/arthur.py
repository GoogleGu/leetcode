# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        if not pHead:
            return None

        void_head = ListNode('#')
        void_head.next = pHead
        last_valid_node = void_head
        this_node = pHead.next
        last_first_node = pHead
        count = 1

        while this_node is not None:
             
            # 当前节点不重复
            if this_node.val != last_first_node.val:
                if count < 2:
                    last_valid_node = last_first_node

                last_first_node = this_node
                count = 1

            
            # 当前节点重复
            else:
                count += 1
                if count > 1:
                    last_valid_node.next = this_node.next
            

            # 前进至下一个节点
            this_node = this_node.next
            
        return void_head.next


if __name__ == "__main__":
    head = ListNode(1)
    node = head
    for val in [2, 3, 3, 4, 4, 5, 6]:
        node.next = ListNode(val)
        node = node.next
    head = Solution().deleteDuplication(head)
    while head:
        print(head.val)
        head = head.next
