public class Solution {
    public int FindGreatestSumOfSubArray(int[] array) {
        int max=array[0];
        for (int i=0;i<array.length;i++){
            int at = 0;
            for (int j =i;j<array.length;j++){
                at+=array[j];
                if (at>max){
                    max = at;
                }
            }
        }
        return max;
    }
}