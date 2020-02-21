# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        fake_head = ListNode(None)
        rear_node = fake_head
        fake_head.next = head
        front_node = fake_head.next
        in_duplicates = False
        while front_node and front_node.next:
            if rear_node.next is front_node:
                front_node = front_node.next
                if front_node.val == rear_node.next.val:
                    in_duplicates = True
                continue
            if not in_duplicates:
                rear_node = rear_node.next
                front_node = front_node.next
                if rear_node.next.val == front_node.val:
                    in_duplicates = True
            else:
                front_node = front_node.next
                if front_node is None:
                    rear_node.next = None
                elif front_node.val != rear_node.next.val:
                    rear_node.next = front_node
                    in_duplicates = False
        if in_duplicates:
            rear_node.next = None
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
    # head.next.next = ListNode(4)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    sol = Solution()
    head = sol.deleteDuplicates(head)
    print_linked_list(head)
