
//前序遍历：根结点 ---> 左子树 ---> 右子树
//
//中序遍历：左子树---> 根结点 ---> 右子树
//
//后序遍历：左子树 ---> 右子树 ---> 根结点

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
    int index = -1;
    String Serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        if(root == null){
            sb.append("#,");
            return sb.toString();
        }
        sb.append(root.val + ",");
        sb.append(Serialize(root.left));
        sb.append(Serialize(root.right));
        return sb.toString();
    }
    TreeNode Deserialize(String str) {
        index++;
        String[] strArr = str.split(",");
        TreeNode node = null;
        if (!strArr[index].equals("#")){
            node = new TreeNode(Integer.valueOf(strArr[index]));
            node.left = Deserialize(str);
            node.right = Deserialize(str);
        }
        return node;
    }
}