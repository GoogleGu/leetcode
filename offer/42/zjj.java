import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> FindNumbersWithSum(int [] array,int sum) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        int i=0,j=array.length-1;
        while(i<j){
            int count = array[i]+array[j];
            if(count==sum){
                list.add(array[i]);
                list.add(array[j]);
                return list;
            }else if(count>sum){
                j--;
            }else{
                i++;
            }
        }
        return list;
    }
}