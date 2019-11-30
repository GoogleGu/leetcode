public class Solution {
    public int cutRope(int target) {
        if (target<2){
            return 0;
        }
        if (target==2){
            return 1;
        }
        if (target==3){
            return 2;
        }
        int remainder = target%3;
        int num = target/3;
        if (remainder==0){
            return (int) Math.pow(3,num);
        }else if (remainder==1){
            return (int) Math.pow(3,num-1)*2*2;
        }else if (remainder==2){
            return (int) Math.pow(3,num)*2;
        }
        return 0;
    }
}