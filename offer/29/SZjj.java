import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
    public ArrayList<Integer> GetLeastNumbers_Solution(int [] input, int k) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        if(input.length < k || k == 0){
            return list;
        }

        int[] minArr= Arrays.copyOf(input,k);
        for (int i = k; i < input.length; i++){
            int[] max= getMax(minArr);
            if (max[1]>input[i]){
                minArr[max[0]]=input[i];
            }
        }
        for (int i = 0; i < k; i++) {
            list.add(minArr[i]);
        }
        return list;
    }

    public int[] getMax(int arr[]){
        int[] max ={0,arr[0]} ;
        for (int i = 1; i < arr.length; i++){
            if(arr[i]>max[1]){
                max[0]=i;
                max[1]=arr[i];
            }
        }
        return max;
    }
}
