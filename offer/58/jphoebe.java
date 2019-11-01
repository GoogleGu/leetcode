import java.util.concurrent.atomic.AtomicInteger;

public class Solution {

    boolean isSymmetrical(TreeNode pRoot) {
        if (pRoot == null){
            return true;
        }
        TreeNode left = pRoot.left;
        TreeNode right = pRoot.right;
        while (left != null && right != null){
            TreeNode leftTemp = left;
            TreeNode rightTemp = right;
            while (leftTemp != null && rightTemp != null){
                if (leftTemp.val != rightTemp.val){
                    return false;
                }
                leftTemp = leftTemp.left;
                rightTemp = rightTemp.right;
            }
            if (!this.compare(leftTemp, rightTemp)){
                return false;
            }
            left = left.right;
            right = right.left;
        }
        return this.compare(left, right);
    }

    public boolean compare(TreeNode left, TreeNode right){
        if ( (left==null && right!=null) || left!=null && right==null ){
            return false;
        }else{
            return true;
        }
    }

}
