import json

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def Serialize(self, root):
        def preorder_traverse(root):
            if root is None:
                result.append('#')
            else:
                result.append(root.val)
                preorder_traverse(root.left)
                preorder_traverse(root.right)

        result = []
        preorder_traverse(root)
        return json.dumps(result)

    def Deserialize(self, s):
        
        def decode(s):
            nonlocal index
            index += 1
            if s[index] != '#':
                node = TreeNode(s[index])
                node.left = decode(s)
                node.right = decode(s)
            else:
                node = None
            return node

        index = -1
        s = json.loads(s)
        return decode(s)
    
        
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.right = TreeNode(5)
    serialized = solution.Serialize(root)
    print(solution.Serialize(root))
    root = solution.Deserialize(serialized)
    print(solution.Serialize(root))