/*
public class TreeLinkNode {
    int val;
    TreeLinkNode left = null;
    TreeLinkNode right = null;
    TreeLinkNode next = null;

    TreeLinkNode(int val) {
        this.val = val;
    }
}
*/
public class SolutionZcsh {
    public TreeLinkNode GetNext(TreeLinkNode pNode)
    {
        if (pNode == null) return null;
        if (pNode.right == null) {
            TreeLinkNode parent = pNode.next;
            while (parent != null && parent.right == pNode) {
                pNode = parent;
                parent = parent.next;
            }
            return parent;
        }
        TreeLinkNode result = pNode.right;
        while (result.left != null) {
            result = result.left;
        }
        return result;
    }
}
