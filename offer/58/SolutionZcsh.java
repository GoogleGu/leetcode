/*
public class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }

}
*/
public class SolutionZcsh {
    boolean isSymmetrical(TreeNode pRoot) {
        if (pRoot == null) return true;
        return check(pRoot.left , pRoot.right);
    }

    boolean check(TreeNode tree1, TreeNode tree2) {
        if (tree1 == null && tree2 == null) return true;
        if (tree1 == null || tree2 == null) return false;
        return tree1.val == tree2.val  && check(tree1.left, tree2.right) && check(tree1.left, tree2.right);
    }
}
