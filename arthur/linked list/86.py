# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        prior = prior_head = ListNode(None)
        post = post_head = ListNode(None)

        while head:
            if head.val < x:
                prior.next = head
                prior = head
            else:
                post.next = head
                post = head
            head = head.next
        prior.next = post_head.next
        post.next = None
        return prior_head.next


def print_linked_list(head):
    ll = []
    while head:
        ll.append(head.val)
        head = head.next
    return ll


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    sol = Solution()
    head = sol.partition(head, 3)
    print(print_linked_list(head))
