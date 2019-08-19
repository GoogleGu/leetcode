public class SolutionZcsh {
    public int TreeDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        int leftLength = TreeDepth(root.left) + 1;
        int rigthLength = TreeDepth(root.right) + 1;
        
        return leftLength > rigthLength ? leftLength : rigthLength;
    }
    
    
}
