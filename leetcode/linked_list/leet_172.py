# Definition for a Node.
class Node:
    def __init__(self, x, next= None, random= None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        node = head
        while node:
            new_node = Node(node.val, node.next, node.random)
            node.next = new_node
            node = node.next.next
        node = head.next
        while node:
            node.random = node.random.next if node.random else None
            if not node.next:
                break
            node = node.next.next

        node = head
        new_head = Node(0)
        new_node = new_head
        while node:
            temp = node.next.next
            new_node.next = node.next
            new_node = new_node.next
            node = temp

        return new_head.next

if __name__ == '__main__':
    from leetcode.linked_list.main import linked_list_to_list
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head = Solution().copyRandomList(head)
    print(linked_list_to_list(head))
