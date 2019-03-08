
class Solution:
    """
    运行时间：24ms
    占用内存：5728k
    """

    push_stack = list()
    pop_stack = list()

    def push(self, node):
        self.transfer_nodes_between_stacks(self.pop_stack, self.push_stack)
        self.push_stack.append(node)

    def pop(self):
        self.transfer_nodes_between_stacks(self.push_stack, self.pop_stack)
        return self.pop_stack.pop()

    @staticmethod
    def transfer_nodes_between_stacks(source_stack, target_stack):
        while source_stack:
            target_stack.append(source_stack.pop())

