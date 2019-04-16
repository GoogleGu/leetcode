#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, pHead):
        if pHead is None:
            return None
        pre = None
        next = None
        ## 交换法则
        while pHead is not None:
            next = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = next
        return pre


value = ListNode({1, 2, 3, 4, 5})
value.next = ListNode({2, 3, 4, 5})
value.next.next = ListNode({3, 4, 5})
value.next.next.next = ListNode({4, 5})
value.next.next.next.next = ListNode({5})

print(Solution().ReverseList(value))
