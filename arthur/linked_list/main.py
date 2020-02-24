class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def linked_list_to_list(head):
    ll = []
    while head:
        ll.append(head.val)
        head = head.next
    return ll


if __name__ == '__main__':
    from arthur.linked_list.leet_172 import Solution, Node
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head = Solution().copyRandomList(head)
    print(linked_list_to_list(head))
