public class Solution {

    TreeNode result = null;
    int index = 0;

    TreeNode KthNode(TreeNode pRoot, int k) {
        this.getList(pRoot, k);
        return index == k ? result : null;
    }

    void getList(TreeNode pRoot, int k) {
        if (pRoot == null) {
            return;
        }
        if (k == index) {
            return;
        }
        if (pRoot.left != null) {
            this.getList(pRoot.left, k);
        }
        if (k == index) {
            return;
        }
        index++;
        result = pRoot;
        if (pRoot.right != null) {
            this.getList(pRoot.right, k);
        }

    }

}
