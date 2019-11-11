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
    
     int index;
     String Serialize(TreeNode root) {
        if (root == null) return "";
        StringBuilder sb = new StringBuilder();
        serialize(root, sb);
        return sb.toString();
    }

    /**
     * 前序遍历
     * @param root
     * @param sb
     */
    public void serialize(TreeNode root, StringBuilder sb) {
        if (root == null) {
            sb.append("#!");
            return;
        }
        sb.append(root.val).append("!");
        serialize(root.left, sb);
        serialize(root.right, sb);
    }

    TreeNode Deserialize(String str) {
        index = -1;
        String[] strArray;
        if (str == null || "".equals(str) || (strArray = str.split("!")).length == 0) return null;

        return deserialize(strArray);
    }

    public TreeNode deserialize(String[] split) {
        index++;
        if (index >= split.length || "#".equals(split[index])) return null;
        TreeNode node = new TreeNode(Integer.valueOf(split[index]));
        node.left = deserialize(split);
        node.right = deserialize(split);
        return node;
    }
}
