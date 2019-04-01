public class Solution {
    public void reOrderArray(int [] array) {
        int[] arrayStack = new int[array.length];
        int left = 0 ;
        int right = 0; // 计算奇偶数 数量
        int length = arrayStack.length - 1;
        for (int i = 0; i <= length; i++) {
            if (( array[i] & 1) == 1) {
                arrayStack[left++] = array[i];
            } else {
                arrayStack[length - right++] = array[i];
            }
        }
        right--;
        for (int i = 0; i <= length; i++) {
            if (i < left) {
                array[i] =  arrayStack[i];
            } else {
                array[left + right--] = arrayStack[i];
            }
        }
    }
}
