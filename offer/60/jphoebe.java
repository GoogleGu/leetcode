import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;


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
    ArrayList<ArrayList<Integer>> Print(TreeNode pRoot) {
        if (pRoot == null){
            return new ArrayList<>();
        }

        int count = 0 , nextLineCount = 1;
        Queue<TreeNode> queue = new LinkedList<>();
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        ArrayList<Integer> line = new ArrayList<>();
        
        queue.offer(pRoot);
        while (!queue.isEmpty()){
            count++;
            TreeNode node = queue.poll();
            line.add(node.val);
            if (node.left != null){
                queue.offer(node.left);
            }
            if (node.right != null){
                queue.offer(node.right);
            }
            if (count == nextLineCount){
                nextLineCount = queue.size();
                count = 0;
                result.add(line);
                line = new ArrayList<>();
            }

        }
        return result;
    }
    
}
