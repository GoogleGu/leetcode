import java.util.ArrayList;
import java.util.LinkedList;
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
    
    private ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
 
    private LinkedList<Integer> linkedList = new LinkedList<Integer>();

    public ArrayList<ArrayList<Integer>> FindPath(TreeNode root, int target) {
        if (root == null || target <= 0)
            return result;

        linkedList.add(root.val);
        if (root.left == null && root.right == null && target == root.val)
            result.add(new ArrayList(linkedList));

        FindPath(root.left ,target - root.val);
        FindPath(root.right ,target - root.val);
        linkedList.removeLast();
        return result;
    }

}









