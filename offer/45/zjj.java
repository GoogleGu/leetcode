import java.util.Arrays;
public class Solution {
    public boolean isContinuous(int [] numbers) {
        if (numbers.length==0){
            return false;
        }
        int zero = 0;
        int num = 0;
        Arrays.sort(numbers);
        for (int i=0;i<numbers.length-1;i++){
            // 统计大小王
            if (numbers[i]==0){
                zero++;
                continue;
            }
            if(numbers[i]==numbers[i+1]){
                return false;
            }
            num+=numbers[i+1]-numbers[i]-1;
        }
        if (zero>=num){
            return true;
        }
        return false;
    }
}