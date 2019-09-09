import java.util.ArrayList;
public class Solution {
        
        public static ArrayList<ArrayList<Integer>> FindContinuousSequence(int sum){
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        int left = 1, right =2;
        while (left<right){
           int temp =  (left+right)*(right-left+1)/2;
           if (temp ==sum){
               ArrayList<Integer> list = new ArrayList<>();
               for (int i = left;i<=right;i++){
                   list.add(i);
               }
               result.add(list);
               left++;
           }else if(temp<sum){
               right++;
           }else if(temp>sum){
               left++;
           }
        }
        return result;
    }

}
