import java.util.LinkedList;
public class Solution {
    public int LastRemaining_Solution(int n, int m) {
        if(n==0){
            return -1;
        }
        LinkedList<Integer> list = new LinkedList<Integer>();
        for (int i = 0; i < n; i ++) {
            list.add(i);
        }
        int reIndex =(m-1)%list.size(); // 第一次要删除的下标
        while (list.size()>1){
            list.remove(reIndex);
            reIndex = (reIndex+(m-1))%list.size();
        }
        return list.get(0);
    }
}