# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        fake_head = ListNode(None)
        fake_head.next = head

        head = fake_head
        while True:
            tail = self.get_tail(head, k)
            if tail is False:
                break
            head = self.reverse_group(head, tail)

        return fake_head.next

    def reverse_group(self, head, tail):

        fake_head = head
        new_head = head = head.next

        next = head.next
        while next is not tail:
            temp = next.next
            next.next = head
            head = next
            next = temp
        fake_head.next = head
        new_head.next = tail

        return new_head

    def get_tail(self, head, k):
        node = head
        for i in range(k+1):
            if node is None:
                return False
            node = node.next
        return node



def print_linked_list(head):
    ll = []
    while head:
        ll.append(head.val)
        head = head.next
    return ll


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    sol = Solution()
    head = sol.reverseKGroup(head, 2)
    print(print_linked_list(head))
