import java.util.ArrayList;
public class Solution {
    public int minNumberInRotateArray(int [] array) {
    
        if (array == null || array.length == 0) {
            return 0;
        }

        for (int i = 1; i < array.length; i++){
            if (array[i] < array[0]){
                return array[i];
            } else if (array[array.length - 1 - i] > array[array.length - 1]){
                return array[array.length - i];
            }
        }
        
        return array[0]; 
    }
    
}
