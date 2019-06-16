public class Solution {
    public int MoreThanHalfNum_Solution(int [] array) {
        if (array.length <= 1){
            return array.length == 1 ? array[0] : 0;
        }
        int val = 0; 
        for (int i = 0,count = Integer.MIN_VALUE; i < array.length - 1; i++) {
            if (array[i] == array[i + 1]) {
                if (count <= 0) {
                    val = array[i];
                    count = 1;
                } else {
                    count = val == array[i] ? count + 1 : count - 1 ;
                }
            }
        }

        return val;
    }
}
