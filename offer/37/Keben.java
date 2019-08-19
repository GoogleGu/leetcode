public class Solution {
    public static int GetNumberOfK(int [] array , int k) {
        int sum = 0;
        for(int temp : array){
            if(temp == k){
                sum++;
            }
        }
        return sum;
    }
}
