class Solution {
    public TreeLinkNode GetNext(TreeLinkNode pNode) {

        if (pNode == null) {
            return null;
        }
        // 有右子树，那么下一个结点就是右子树最左边的节点。
        if (pNode.right != null) {
            pNode = pNode.right;
            while (pNode.left != null) {
                pNode = pNode.left;
            }
            return pNode;
        }
        // 有右子树
        while (pNode.next != null) {
            if (pNode.next.left == pNode) {
                return pNode.next;
            }
            pNode = pNode.next;
        }
        return null;
    }
}
