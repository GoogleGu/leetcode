import java.util.Arrays;
public class SolutionZcsh {
    private int[] originArray;
    private int[] copyArray;
    
    
    public int InversePairs(int [] array) {
        if (array == null || array.length == 0) {
            return 0;
        }

        originArray = array;
        copyArray = Arrays.copyOf(array, array.length);

        return exec(0,array.length -1) % 1000000007;
    }

    public int exec(int start, int end) {

        if (end == start) {
            return 0;
        }

        int middle = (end + start) >> 1;
        int result = (exec(start, middle) % 1000000007) + (exec(middle + 1, end) % 1000000007 );

        int i = middle;
        int j = end;
        int index = end;
        while (j > middle && i >= start) {
            if (originArray[i] > originArray[j]) {
                result += j - middle;
                if (result >= 1000000007) {
                    result %= 1000000007;
                } 
                copyArray[index--] = originArray[i--];
            } else {
                copyArray[index--] = originArray[j--];
            }

        }

        while (j > middle) {
            copyArray[index--] = originArray[j--];
        }

        while (i >= start) {
            copyArray[index--] = originArray[i--];
        }

        for (int k = start; k <= end; k++) {
            originArray[k] = copyArray[k];
        }

        return result % 1000000007;
    }


}
