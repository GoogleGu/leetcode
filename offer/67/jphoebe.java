public class Solution {
    public int cutRope(int target) {
        if (target < 0) {
            return 0;
        } else if (target == 2) {
            return 1;
        } else if (target == 3) {
            return 2;
        } else{
            int list[] = new int[target + 1];
            list[0] = 0;
            list[1] = 1;
            list[2] = 2;
            list[3] = 3;
            for (int i = 4; i <= target; i++) {
                int max = 0;
                for (int j = 1; j <= i / 2; j++) {
                    int temp = list[j] * list[i - j];
                    if (max < temp) {
                        max = temp;
                    }
                }
                list[i] = max;
            }
            return list[target];
        }
    }
}
