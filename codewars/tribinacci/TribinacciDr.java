package tribinacci;

import java.util.Arrays;

/**
 * @author Dream
 * @date 2018/12/6 10:41
 */
public class TribinacciDr {

    public double[] tribonacci(double[] s, int n) {
        double[] arr = Arrays.copyOf(s, n);
        for (int i = s.length; i < arr.length; i++) {
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3];
        }
        return arr;
    }
}
