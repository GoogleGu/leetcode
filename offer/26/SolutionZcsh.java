public class SolutionZcsh {
    public TreeNode Convert(TreeNode pRootOfTree) {

        TreeNode head = new TreeNode(-1);
        execute(pRootOfTree, head);
        if (head.right == null) {
            return pRootOfTree;
        }
        head = head.right;
        head.left = null;
        return head;
    }

    public TreeNode execute(TreeNode pRootOfTree, TreeNode head) {

        if (pRootOfTree != null) {
            head = execute(pRootOfTree.left, head);
            head = swap(head, pRootOfTree);
            head = execute(pRootOfTree.right, head);
        }
        return head;

    }

    private TreeNode swap(TreeNode head, TreeNode nextNode) {
        if (nextNode == null) {
            return head;
        }
        head.right = nextNode;
        nextNode.left = head;
        return nextNode;
    }
}
