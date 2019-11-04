import java.util.ArrayList;
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
    public ArrayList<ArrayList<Integer> > Print(TreeNode pRoot) {
        ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
        // 第几层
        int number = 1;
        // 奇数层的数据
        Stack<TreeNode> odd = new Stack<>();
        // 偶数层的数据
        Stack<TreeNode> even = new Stack<>();
        odd.push(pRoot); // 先把第一层存进去
        while (!odd.empty()||!even.empty()){
            if (number%2!=0){ // 奇数层
                // 这一层的数据
                ArrayList<Integer> thisData = new ArrayList<Integer>();
                while (!odd.empty()){
                    // 取出奇数层里存的数据 并把它拿走
                    TreeNode thisNode = odd.pop();
                    if (thisNode!=null){
                        thisData.add(thisNode.val); // 把值放入临时的数组中  并把下一层存入偶数层
                        even.push(thisNode.left); //从左
                        even.push(thisNode.right); //到右
                    }
                }
                if (!thisData.isEmpty()){
                    list.add(thisData);// 存入最终数据中
                    number++; // 层数加1
                }
            }else {
                // 这一层的数据
                ArrayList<Integer> thisData = new ArrayList<Integer>();

                while (!even.empty()){
                    // 取出偶数层里存的数据 并把它拿走
                    TreeNode thisNode = even.pop();
                    if (thisNode!=null){
                        thisData.add(thisNode.val);// 把值放入临时的数组中  并把下一层存入奇数层
                        odd.push(thisNode.right); // 从右
                        odd.push(thisNode.left); //到左
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