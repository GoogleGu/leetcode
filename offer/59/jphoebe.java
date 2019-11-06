import java.util.*;

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
    Stack<TreeNode> odd = new Stack<>();
    Stack<TreeNode> even = new Stack<>();
    int count = 0 , nextLineCount = 1, lineNumber = 1;
    ArrayList<ArrayList<Integer>> result = new ArrayList<>();
    ArrayList<Integer> line = new ArrayList<>();

    public ArrayList<ArrayList<Integer>> Print(TreeNode pRoot) {
        if (pRoot == null){
            return new ArrayList<>();
        }
        odd.add(pRoot);
        while (!odd.isEmpty() || !even.isEmpty() ){
            count ++;
            TreeNode node;
            if (lineNumber % 2 == 1){
                // 下一行偶数行 右遍历
                node = odd.pop();
                line.add(node.val);
                if (node.left != null){
                    even.add(node.left);
                }
                if (node.right != null){
                    even.add(node.right);
                }

                if (count == nextLineCount){
                    nextLineCount = even.size();
                    count = 0;
                    lineNumber ++;
                    result.add(line);
                    line = new ArrayList<>();
                }
            }else{
                // 下一行技术行 左遍历
                node = even.pop();
                line.add(node.val);
                if (node.right != null){
                    odd.add(node.right);
                }
                if (node.left != null){
                    odd.add(node.left);
                }

                if (count == nextLineCount){
                    nextLineCount = odd.size();
                    count = 0;
                    lineNumber ++;
                    result.add(line);
                    line = new ArrayList<>();
                }
            }

        }
        return result;
    }

}
