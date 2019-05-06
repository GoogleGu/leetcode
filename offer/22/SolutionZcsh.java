import java.util.ArrayList;
import java.util.concurrent.LinkedBlockingQueue;

public class Solution {
    public ArrayList<Integer> PrintFromTopToBottom(TreeNode root) throws InterruptedException {
        ArrayList<Integer> arrayList = new ArrayList<Integer>();
        if (root == null) {
            return arrayList;
        }

        LinkedBlockingQueue<TreeNode> queue = new LinkedBlockingQueue();
        queue.put(root);
        while (true && !queue.isEmpty()) {
            TreeNode poll = queue.poll();
            arrayList.add(poll.val);
            if (poll.left != null) {
                queue.put(poll.left);
            }
            if (poll.right != null) {
                queue.put(poll.right);
            }
        }

        return arrayList;
    }

}
