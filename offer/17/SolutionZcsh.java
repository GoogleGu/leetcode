/**
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
    public boolean HasSubtree(TreeNode root1,TreeNode root2) {
        if (root2 == null || root1 == null) {
            return false;
        }
        return equalsNode(root1, root2) 
            || HasSubtree(root1.left , root2) // 考虑节点相同情况
            || HasSubtree(root1.right , root2);
    }
    
    // 递归节点,判断是否相同.一开始没理解节点看看重复,并且只是包含子节点,即中间包含的节点,不是尾部
    public Boolean equalsNode(TreeNode root1,TreeNode root2) {
        return root2 == null ? true :  //  r2 遍历结束,r1 还没有. r1 中包含 r2
               root1 == null ?  false : // r1 遍历结束,r2还没结束, r2 多余 r1
               root1.val != root2.val ? false : // r1 r2 内容不同
               equalsNode(root1.left, root2.left) && equalsNode(root1.right, root2.right); // 该节点相同,比较子节点
    }
}





