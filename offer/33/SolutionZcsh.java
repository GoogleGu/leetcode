
public class Solution {
    
    public int GetUglyNumber_Solution(int index) {

        if (index < 7)
            return index;

        int[] result = new int[index];
        result[0] = 1;
        int t2 = 0, t3 = 0, t5 = 0;
        for (int i = 1; i < index; i++) {
            result[i] = Math.min(result[t2] * 2, Math.min(result[t3] * 3, result[t5] * 5));
            if (result[t2] * 2 == result[i]) t2++;
            if (result[t3] * 3 == result[i]) t3++;
            if (result[t5] * 5 == result[i]) t5++;
        }
        return result[index - 1];

    }

}
