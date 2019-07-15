import java.util.ArrayList;

public class Solution {
    public String PrintMinNumber(int [] numbers) {
        int min = Integer.MAX_VALUE;
        for (int i=0;i<numbers.length;i++){
            for (int j=i+1;j<numbers.length;j++){
                int num1 = Integer.valueOf(numbers[i]+""+numbers[j]);
                int num2 = Integer.valueOf(numbers[j]+""+numbers[i]);
                if (num1>num2){
                    int z = numbers[i];
                    numbers[i] = numbers[j];
                    numbers[j] = z;
                }
            }
        }
        StringBuffer stringBuffer = new StringBuffer();
        for (int k=0;k<numbers.length;k++){
            stringBuffer.append(numbers[k]);
        }
        return String.valueOf(stringBuffer);
    }
}