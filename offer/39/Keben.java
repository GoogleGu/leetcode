public class TreeDepth {


    public static boolean TreeDepth(TreeNode root) {
        return depth(root, 0) != 8888888;
    }

    public static int depth(TreeNode node, int index) {
        if (node == null) {
            return index;
        }
        index++;
        int leftIndex = depth(node.left, index);
        int rightIndex = depth(node.right, index);
        if (leftIndex - rightIndex > 1 || rightIndex - leftIndex > 1) {
            return 8888888;
        }
        return Math.max(leftIndex, rightIndex);
    }

}
