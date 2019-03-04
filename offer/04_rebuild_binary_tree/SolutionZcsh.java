public class Solution {
   public  static TreeNode reConstructBinaryTree(int[] pre, int[] in) {
       TreeNode node = createTree(pre,0,pre.length -1 , in, 0, in.length - 1);
       return node;
    }
    
    public static TreeNode createTree(int[] pre,int startPre, int endPre,
                                int[] in, int startIn, int endIn) {
        if (startPre > endPre || startIn > endIn) {
            return null;
        }
        int currentValue = pre[startPre];
        TreeNode node = new TreeNode(currentValue);
        for (int i = startIn; i <= endIn ; i++) {
            if (in[i] == currentValue) {
                node.left = createTree(pre, startPre + 1, startPre + i - startIn  ,
                                       in ,startIn , i - 1);
                node.right = createTree(pre ,endPre - endIn + i  + 1, endPre, 
                                        in, i + 1, endIn);
            }
        }
        
        return node;
    }
}
