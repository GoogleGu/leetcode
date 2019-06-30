public class Solution {
    public int FindGreatestSumOfSubArray(int[] array) {
        int maxValue = Integer.MIN_VALUE;
        for (int i = 0, tempSum = 0; i < array.length; i++) {
            tempSum += array[i];
            maxValue = tempSum >= maxValue ? tempSum : maxValue;
            if (tempSum < 0) {
                tempSum = 0;
            }
        }

        return maxValue;
    }
}
