# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        fake_head = ListNode(None)
        fake_head.next = head
        node = fake_head
        while node.next:
            if node.next.next and node.next.val == node.next.next.val:
                tmp_node = node.next.next
                while tmp_node and tmp_node.val == node.next.val:
                    tmp_node = tmp_node.next
                node.next = tmp_node
            else:
                node = node.next

        return fake_head.next


def print_linked_list(head):
    ll = []
    while head:
        ll.append(head.val)
        head = head.next
    print(ll)
    return ll


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    sol = Solution()
    head = sol.deleteDuplicates(head)
    print_linked_list(head)
