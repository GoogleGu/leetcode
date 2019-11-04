import java.util.ArrayList;
import java.util.Stack;
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
    public ArrayList<ArrayList<Integer>> Print(TreeNode pRoot) {

        if (pRoot == null) return new ArrayList<>();

        ArrayList<ArrayList<Integer>> resultList = new ArrayList<>();
        Stack<TreeNode> leftToRight = new Stack<>();
        Stack<TreeNode> rightToLeft = new Stack<>();
        // 第一行从左向右
        leftToRight.push(pRoot);
        for (int i = 1; !(leftToRight.isEmpty() && rightToLeft.empty()); i++) {
            ArrayList<Integer> currentLayer = new ArrayList();
            if ((i & 1) == 1) {
                while (!leftToRight.isEmpty()) {
                    TreeNode pop = leftToRight.pop();
                    currentLayer.add(pop.val);
                    if (pop.left != null) rightToLeft.push(pop.left);
                    if (pop.right != null) rightToLeft.push(pop.right);
                }
            } else {
                while (!rightToLeft.isEmpty()) {
                    TreeNode pop = rightToLeft.pop();
                    currentLayer.add(pop.val);
                    if (pop.right != null) leftToRight.push(pop.right);
                    if (pop.left != null) leftToRight.push(pop.left);
                }
            }
            resultList.add(currentLayer);
        }

        return resultList;
    }
}
