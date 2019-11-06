public class Solution {

    public boolean isSymmetrical(TreeNode pRoot) {
        if (pRoot == null) {  // 空,输出true
            return true;
        }

        return bj(pRoot.left, pRoot.right);
    }

    public boolean bj(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        }

        if (left == null || right == null) {
            return false;
        }
        if (left.val != right.val) {
            return false;
        }
        
        return bj(left.left, right.right) && bj(left.right, right.left);
    }
}
