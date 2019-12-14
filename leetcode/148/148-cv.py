# -*- coding:utf-8 -*-

# 题目url: https://leetcode-cn.com/problems/sort-list/
# 描述：在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。


# 为满足 时间 O(nlogn) 空间 O(1)
#   采用自底而上的归并排序
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def sortList(self, head: ListNode):
        # 计算链表长度
        h, length = head, 0
        while h: 
            h, length = h.next, length + 1

        res = ListNode(-1)
        res.next = head
        # 步长
        intv = 1
        while intv < length:
            pre, h = res, res.next
            while h:
                # 拿到第一个节点
                h1, i = h, intv
                while i and h:
                    h, i = h.next, i - 1

                # h2已为空，循环结束
                if i: 
                    break
                
                # 拿到第二个节点
                h2, i = h, intv
                while i and h: 
                    h, i = h.next, i - 1

                # 合并两节点
                c1, c2 = intv, intv - i 
                while c1 and c2:
                    if h1.val < h2.val: 
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else: 
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                # 跳过多余节点
                while c1 > 0 or c2 > 0: 
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h 
            
            intv *= 2   

        return res.next



# 4->2->1->3
