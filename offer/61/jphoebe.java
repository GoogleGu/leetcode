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
public class Solution {
    StringBuffer result = new StringBuffer();
    int index = -1;
    String[] strSplit = null;

    String Serialize(TreeNode root) {
        if (root == null){
            return result.append("#!").toString();
        }
        result.append(root.val).append("!");
        this.Serialize(root.left);
        this.Serialize(root.right);
        return result.toString();
    }

    TreeNode Deserialize(String str) {
        strSplit = str.split("!");
        TreeNode node = null;
        index++;
        if(!strSplit[index].equals("#")) {
            node = new TreeNode(Integer.valueOf(strSplit[index]));
            node.left = Deserialize(str);
            node.right = Deserialize(str);

        }
        return node;
    }
}
