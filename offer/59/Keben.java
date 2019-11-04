
import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;
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
        public ArrayList<ArrayList<Integer>> Print(TreeNode pRoot) {
                ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        List<TreeNode> leaveList = new ArrayList<>(); // 级别

        if (pRoot!=null){
            leaveList.add(pRoot);
        } 
        boolean isLeftHead = true;
        while (!leaveList.isEmpty()){
            ArrayList<Integer> tempList = new ArrayList<>();

            if (isLeftHead) {
                for (TreeNode treeNode : leaveList) {
                    tempList.add(treeNode.val);
                }
            }else {
                for (int i = leaveList.size()-1; i >= 0; i--) {
                    tempList.add(leaveList.get(i).val);
                }
            }
            list.add(tempList);
            isLeftHead = !isLeftHead;
            
            List<TreeNode> tempLeaveList = new ArrayList<>();
            for (TreeNode treeNode : leaveList) {
                if (treeNode.left != null) {
                    tempLeaveList.add(treeNode.left);
                }
                if (treeNode.right == null) {
                    continue;
                }
                tempLeaveList.add(treeNode.right);
            }
            leaveList.clear();
            leaveList.addAll(tempLeaveList);

        }


        return list;
        }
}
