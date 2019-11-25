import java.util.*;

/**
 * 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
 */
public class Solution {
    public ArrayList<Integer> maxInWindows(int [] num, int size)
    {
        int numLen = num.length;
        ArrayList list = new ArrayList<>();
        if (numLen<size||size<=0){
            return list;
        }
        for (int i =0;i+size<=numLen;i++){
            ArrayList numList = new ArrayList();
            int count = size;
            for (int j=0;count>0;j++,count--){
                numList.add(num[i+size-j-1]);
            }
            list.add(getMax(numList));
        }
        return list;
    }

    int getMax(ArrayList<Integer> arr){
        int max = arr.get(0);
        for (int i=0;i<arr.size();i++){
            if (max<arr.get(i)){
                max = arr.get(i);
            }
        }
        return max;

    }
}