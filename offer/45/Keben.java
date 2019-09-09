import java.util.Collections;
import java.util.HashSet;
public class Solution {
    /**
     * 是否抽中
     *
     * @param numbers
     * @return
     */
   public static boolean isContinuous(int[] numbers) {
        if(numbers.length == 0) return false;
        HashSet<Integer> set = new HashSet<>();
        int max = -1;
        int min = 14;
        for (int number : numbers) {
            if (!set.add(number) && number != 0) {
                return false;
            }

           if(number!=0){
                max = Math.max(max, number);
                min = Math.min(min,number );
           }
        }
        if ((max-min)<=4){
            return true;
        }
        return false;
    }
}
