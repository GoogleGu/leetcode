public class Solution {
    public int Sum_Solution(int n) {
        int num=n;
        Boolean b =(n>0)&&((num+=Sum_Solution(n-1))>0);
        return num;

    }
}