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
// 中序遍历正好符合 左中右
public class Solution {
    int index = 0;

    TreeNode KthNode(TreeNode pRoot, int k) {
        if(pRoot==null){
            return null;
        }
       
        TreeNode leftNode = KthNode(pRoot.left,k);
        if(leftNode != null){
            return leftNode;
        }
        
        index ++;
        if(index == k){
            return pRoot;
        }

        TreeNode rightNode = KthNode(pRoot.right,k);
        if(rightNode != null){
            return rightNode;
        }
       
        return null;
    }

}
