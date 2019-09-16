public class Solution {
    public int Add(int num1,int num2) {

        while (num2!=0){
            int result= num1^num2;
            num2 = (num1&num2)<<1;
            num1=result;
        }
        return num1;
    }
}