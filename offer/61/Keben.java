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
    int index;
    public String Serialize(TreeNode root) {
         
        StringBuffer sb = new StringBuffer();
        if(root == null){
            sb.append("#,");
            return sb.toString();
        }
        sb.append(root.val+",");
        sb.append(Serialize(root.left));
        sb.append(Serialize(root.right));
        return sb.toString();
         
  }
    public TreeNode Deserialize(String str) {
        
        //先判空
        if(str == null){
            return null;
        }
        index = -1;
        String[] strSeg = str.split(",");
         
        return DeserializeStr(strSeg);
         
  }
    public TreeNode DeserializeStr(String[] strSeg){
         
        index++;
        TreeNode treeNode = null;
        if(!strSeg[index].equals("#")){
            treeNode = new TreeNode(Integer.valueOf(strSeg[index]));
            treeNode.left = DeserializeStr(strSeg);
            treeNode.right = DeserializeStr(strSeg);
        }
         
        return treeNode;
    }
     
}
