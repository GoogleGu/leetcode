public class Solution {
    // 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
    public boolean IsBalanced_Solution(TreeNode root) {
        return IsBalance(root)!=0;

    }
    // 0不平衡  1平衡
    private int IsBalance(TreeNode root){
        if (root==null){
            return 1;
        }
        int left = IsBalance(root.left);
        if (left==0){
            return 0;
        }
        int right = IsBalance(root.right);
        if (right==0){
            return 0;
        }
        return Math.abs(right-left)>1?0:Math.max(right,left)+1;
    }
}