import java.util.Arrays;
import java.util.Comparator;

public class Solution {
    public String PrintMinNumber(int [] numbers) {
        StringBuilder sb = new StringBuilder();
        Integer[] array = new Integer[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            array[i] = numbers[i];
        }
        
        Arrays.sort(array, (Comparator<Integer>) (a, b) -> {
            String s1 = a + "" + b;
            String s2 = b + "" + a;
            return s1.compareTo(s2);
        });

        for (int i = 0; i < array.length; i++) {
            sb.append(array[i]);
        }

        return sb.toString();
    }
}
