import java.util.ArrayList;
import java.util.concurrent.LinkedBlockingQueue;

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
public class SolutionZcsh {
    ArrayList<ArrayList<Integer> > Print(TreeNode pRoot) {
        if (pRoot == null) return new ArrayList<>();
        ArrayList<ArrayList<Integer>> resultList = new ArrayList<>();
        LinkedBlockingQueue<TreeNode> forEcho = new LinkedBlockingQueue<>();
        forEcho.add(pRoot);
        while (!forEcho.isEmpty()) {
            LinkedBlockingQueue<TreeNode> itemQueue = new LinkedBlockingQueue<>();
            ArrayList<Integer> valueList = new ArrayList<>();
            TreeNode current;
            while ((current = forEcho.poll()) != null) {
                valueList.add(current.val);
                if (current.left != null) itemQueue.add(current.left);
                if (current.right != null) itemQueue.add(current.right);
            }
            forEcho = itemQueue;
            if (!valueList.isEmpty()) resultList.add(valueList);
        }
        return resultList;
    }
    
}
