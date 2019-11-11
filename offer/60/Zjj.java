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
    ArrayList<ArrayList<Integer> > Print(TreeNode pRoot) {
        ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
        // 第几层
        int number = 1;
        // 奇数层的数据
        Queue<TreeNode> odd = new LinkedList<TreeNode>();
        // 偶数层的数据
        Queue<TreeNode> even = new LinkedList<TreeNode>();
        odd.add(pRoot);// 先把第一层存进去
        while (odd.size()>0||even.size()>0){
            if (number%2!=0){ // 奇数层
                // 这一层的数据
                ArrayList<Integer> thisData = new ArrayList<Integer>();
                while (odd.size()>0){
                    // 取出奇数层里存的数据 并把它拿走
                    TreeNode thisNode = odd.poll();
                    if (thisNode!=null){
                        thisData.add(thisNode.val); // 把值放入临时的数组中  并把下一层存入偶数层
                        even.add(thisNode.left); //从左
                        even.add(thisNode.right); //到右
                    }
                }
                if (!thisData.isEmpty()){
                    list.add(thisData);// 存入最终数据中
                    number++; // 层数加1
                }
            }else {
                // 这一层的数据
                ArrayList<Integer> thisData = new ArrayList<Integer>();

                while (even.size()>0){
                    // 取出偶数层里存的数据 并把它拿走
                    TreeNode thisNode = even.poll();
                    if (thisNode!=null){
                        thisData.add(thisNode.val);// 把值放入临时的数组中  并把下一层存入奇数层
                        odd.add(thisNode.left);
                        odd.add(thisNode.right);
                    }
                }

                if (!thisData.isEmpty()){
                    list.add(thisData);
                    number++; // 层数加1
                }
            }
        }
        return list;
    }

}