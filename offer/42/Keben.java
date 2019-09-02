import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> FindNumbersWithSum(int [] array,int sum) {
        ArrayList<Integer> list = new ArrayList<>();
        int left = 0,right = array.length-1;
        while(left < right){
            int total = array[left]+array[right];
            if(total==sum){
                list.add(array[left]);
                list.add(array[right]);
                break;
            }else if(total>sum){
                right--;
            }else if(total<sum){
                left++;
            }
        }
        return list;

    }
}
