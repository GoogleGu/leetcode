#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        if head is None:
            return None
        if k == 0:
            return None
        stack = []
        while head is not None:
            stack.insert(0, head)
            head = head.next
        length = len(stack)
        if length < k:
            return None
        return stack[k - 1]


value = ListNode({1, 2, 3, 4, 5})
value.next = ListNode({2, 3, 4, 5})
value.next.next = ListNode({3, 4, 5})
value.next.next.next = ListNode({4, 5})
value.next.next.next.next = ListNode({5})

print(Solution().FindKthToTail(value, 1));
