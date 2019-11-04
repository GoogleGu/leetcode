
//左子树的左子树和右子树的右子树相同  左子树的右子树和右子树的左子树相同
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
    boolean isSymmetrical(TreeNode pRoot)
    {
        if (pRoot == null){
            return true; // 如果是空  一定是对称的
        }
        return comparison(pRoot.left,pRoot.right);
    }

    private boolean comparison(TreeNode leftNode,TreeNode rightNode){
        if (leftNode==null){
            if (rightNode==null){ //左边的节点是空  右边的节点也是空 那就是对称的
                return true;
            }else {
                return false;  // 左边没有  右边有  就不是对称的
            }
        }
        if (rightNode==null){ // 走到这一步说明左边一定有了 直接就不是
            return false;
        }
        if (leftNode.val!=rightNode.val){ //俩边值不一样也是不对称的
            return false;
        }
        // 如果值一样 就继续比对左节点的右边 和 右节点的左边 和  左节点的左边   和右节点右边
        return comparison(leftNode.right,rightNode.left)&&comparison(leftNode.left,rightNode.right);
    }
}

