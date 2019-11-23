import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> maxInWindows(int [] num, int size)
    {
        if (num == null || num.length == 0 || size == 0 || num.length < size) {
            return new ArrayList<>();
        }
        ArrayList<Integer> result = new ArrayList<>();
        Integer windowMaxValue = null;
        for (int i = size-1; i < num.length; i++) {
            if (windowMaxValue == null) {
                windowMaxValue = num[i];
            }
            for (int j = 1; j < size; j++) {
                if (num[i-j] > windowMaxValue) {
                    windowMaxValue = num[i-j];
                }
            }
            result.add(windowMaxValue);
            windowMaxValue = null;
        }
        return result;
    }
}
