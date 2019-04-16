#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        elif pHead2 is None:
            return pHead1
        new_head = None
        current = None
        while pHead1 is not None and pHead2 is not None:
            value1 = pHead1.val
            value2 = pHead2.val
            if current is None:
                if value1 <= value2:
                    current = pHead1
                    pHead1 = pHead1.next
                else:
                    current = pHead2
                    pHead2 = pHead2.next
                new_head = current
            else:
                current_value = current.val
                if value1 >= current_value and value1 <= value2:
                    current.next = pHead1
                    pHead1 = pHead1.next
                else:
                    current.next = pHead2
                    pHead2 = pHead2.next
                current = current.next
        last_head = None
        if pHead1 is not None:
            last_head = pHead1
        elif pHead2 is not None:
            last_head = pHead2
        current.next = last_head
        return new_head


value1 = ListNode(1)
value1.next = ListNode(2)
value1.next.next = ListNode(3)
value1.next.next.next = ListNode(4)
value1.next.next.next.next = ListNode(5)

value2 = ListNode(1)
value2.next = ListNode(2)
value2.next.next = ListNode(3)
value2.next.next.next = ListNode(4)
value2.next.next.next.next = ListNode(5)

print(Solution().Merge(value1, value2))
