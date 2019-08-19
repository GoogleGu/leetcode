public class SolutionZcsh {
    private boolean flag = true;
    public boolean IsBalanced_Solution(TreeNode root) {
        
        TreeDepth(root);
        return flag;
    }
    
    public int TreeDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        int leftLength = TreeDepth(root.left) + 1;
        int rigthLength = TreeDepth(root.right) + 1;
        
        if (flag) {
            flag = leftLength + 1 == rigthLength ||  leftLength -1 == rigthLength || leftLength == rigthLength;
        }
        
        return leftLength > rigthLength ? leftLength : rigthLength;
    }
}
