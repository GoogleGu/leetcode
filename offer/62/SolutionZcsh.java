public class SolutionZcsh {
    
    private int index;
    
    TreeNode KthNode(TreeNode pRoot, int k)
    {
        index = k;
        return KthNode(pRoot);
    }
    
    TreeNode KthNode(TreeNode pRoot) {
        if (pRoot == null) return pRoot;
        TreeNode node = KthNode(pRoot.left);
        if (node != null) return node;
        if (--index == 0) return pRoot;
        node = KthNode(pRoot.right);
        if (node != null) return node;
        return null;
    }


}
