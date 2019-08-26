//num1,num2分别为长度为1的数组。传出参数
//将num1[0],num2[0]设置为返回结果
public class SolutionZcsh {
    public void FindNumsAppearOnce(int [] array,int num1[] , int num2[]) {
        int result = 0;
        for (int i = 0; i < array.length; i++) {
            result ^= array[i];
        }
        
        int index = 1;
        while ((index & result) == 0) {
            index <<= 1;
        }
        
        for (int i = 0; i < array.length; i++) {
            if ((array[i] & index) == 0) {
                num1[0] ^= array[i];
            } else {
                num2[0] ^= array[i];
            }
        }
        
    }
}
