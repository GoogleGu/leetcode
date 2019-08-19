
public class TreeDepth {


    public static void main(String[] args) {

    }

    public int TreeDepth(TreeNode root) {
        return depth(root, 0);
    }

    public int depth(TreeNode node, int index) {
        if (node == null) {
            return index;
        }
        index++;
        int leftIndex = depth(node.left, index);
        int rightIndex = depth(node.right, index);
        return Math.max(leftIndex, rightIndex);
    }
}
