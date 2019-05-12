public class Solution {
    public boolean VerifySquenceOfBST(int[] sequence) {

        if (sequence.length == 0) {
            return false;
        }

        return VerifySquenceOfBST(sequence, 0, sequence.length - 1);
    }

    public boolean VerifySquenceOfBST(int[] s, int start, int end) {

        if (end <= start) {
            return true;
        }

        int middle = start;
        while (s[end] > s[middle]) middle++;
        for (int i = middle; i < end; i++) {
            if (s[i] < s[end]) {
                return false;
            }
        }
        return VerifySquenceOfBST(s, start, middle - 1) && VerifySquenceOfBST(s, middle, end - 1);
    }
}
