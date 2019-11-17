import java.util.*;
//    二叉查找树（Binary Search Tree），（又：二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。
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
    List<TreeNode> listpx = new ArrayList<>();
    TreeNode KthNode(TreeNode pRoot, int k)
    {
        if (pRoot==null){
            return null;
        }
        if (k<=0){
            return null;
        }
        listpx = mySort(pRoot);
        if(k>=listpx.size()+1){
            return null;
        }
        return listpx.get(k-1);
    }

    public List<TreeNode> mySort(TreeNode root){
        if (root==null){
            return null;
        }
        mySort(root.left);
        listpx.add(root);
        mySort(root.right);
        return listpx;
    }

}