import java.util.ArrayList;
public class Solution {
    public int[] multiply(int[] A) {

        int[] positiveSequence = new int[A.length], invertedSequence =  new int[A.length];

        positiveSequence[0] = 1; // 前半段的积
        invertedSequence[A.length - 1] = 1; // 后半段的积

        for (int i = 1, j = A.length - 2; i < A.length; i++,j--) {
            positiveSequence[i] = positiveSequence[i - 1] * A[i - 1];
            invertedSequence[j] =  invertedSequence[j + 1] * A[j + 1];
        }

        for (int i = 0; i < A.length; i++) {
            A[i] = positiveSequence[i] * invertedSequence[i];
        }
        return A;
    }
}
