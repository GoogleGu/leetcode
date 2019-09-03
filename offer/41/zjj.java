import java.util.ArrayList;
public class Solution {
    public ArrayList<ArrayList<Integer> > FindContinuousSequence(int sum) {
        ArrayList<ArrayList<Integer> > result = new ArrayList<>();
        int start=1;
        int end =2;
        while(start<end){
            int count = (start + end) * (end - start + 1) / 2;
            if(sum==count){
                ArrayList<Integer> list = new ArrayList<>();
                for(int i=start;i<=end;i++){
                    list.add(i);
                }
                result.add(list);
                start++;
            }else if(count < sum){
                end++;
            }else{
                start++;
            }

        }
        return result;

    }
}