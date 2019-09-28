import java.util.ArrayList;
public class Solution {
    public static int[] multiply(int[] A) {
        int[] ass = new int[A.length];
        for (int i = 0; i < A.length; i++) {
            int sum = 1;
            for (int j = 0; j < A.length; j++) {
                if (i == j) {
                    continue;
                }
                if (A[j] == 0) {
                    sum = 0;
                }
                sum *= A[j];
            }
            ass[i] = sum;
        }

        return ass;
    }
}
