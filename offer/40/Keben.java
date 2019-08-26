import java.util.*;
public class Solution {
    public void FindNumsAppearOnce(int[] array, int num1[], int num2[]) {
        Set<Integer> set = new HashSet<>();
        for (int i : array) {
            if (!set.add(i)) {
                set.remove(i);
            }
        }
        
        Iterator<Integer> iterator = set.iterator();
        num1[0] = iterator.next();
        num2[0] = iterator.next();
    }
}
