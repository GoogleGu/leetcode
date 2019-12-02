/**
 * 根据贪婪算法, 当绳子<=3 时,可知,裁剪2段,1*2
 * 大于4时, 每次减3段 可保证最大乘积.
 * 等于4时,最大乘积.4
 */
public class Solution {
  
 public int cutRope(int target) {
        int max=1;
         if(target<=3){
            return target-1;
        }
        while(target>4){
            target-=3;
            max*=3;
        }
        return max*target;
    }
}
