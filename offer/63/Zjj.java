import java.util.*;
public class Solution {

    List<Integer> myList = new ArrayList();
    public void Insert(Integer num) {
        myList.add(num);
    }
    public Double GetMedian() {
        double returnNum=0;
        Collections.sort(myList);
        int size = myList.size();
        if (size%2==1){
            returnNum = myList.get((size-1)/2);
        }else {
            returnNum = ((double)myList.get(size/2)+ (double)myList.get(size/2-1))/2;
        }
        return returnNum;
    }
}